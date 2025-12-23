<template>
    <v-container>
      <v-card outlined>
        <v-card-title class="headline">Routes</v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item v-for="route in routes" :key="route.id">
                <v-list-item-title>
                  {{ route.walls }} Grade: {{ route.grade }} - holds color: {{ route.color }} - {{route.setter_id}}
                </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-title>Add a New Route</v-card-title>
        <v-card-text>
          <v-form ref="routeForm" @submit.prevent="submitRoute">
            <v-text-field
              label="Route Name"
              v-model="newRoute.name"
              required
            ></v-text-field>
            <v-text-field
              label="Grade"
              v-model="newRoute.grade"
              required
            ></v-text-field>
            <v-text-field
              label="Holds Color"
              v-model="newRoute.color"
              required
            ></v-text-field>
            <v-text-field
              label="Created Date"
              v-model="newRoute.date_set"
              type="date"
              required
            ></v-text-field>
            <v-select
              label="Assign to Wall"
              v-model="newRoute.wall_id"
              :items="walls"
              item-text="name"
              item-value="wall_id"
              required
            ></v-select>
            <v-select
              label="Assign Setter"
              v-model="newRoute.setter_id"
              :items="setters"
              item-text="username"
              item-value="setter_id"
              required
            ></v-select>
            <v-btn color="primary" type="submit">Add Route</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "RoutesPage",
    data() {
      return {
        API_BASE_URL: "http://localhost:8000/api",
        routes: [],
        walls: [],
        setters: [],
        newRoute: {
          name: "",
          grade: "",
          color: "",
          date_set: "",
          wall_id: null,
          setter_id: null,
        },
      };
    },
    created() {
      this.fetchRoutes();
      this.fetchWalls();
      this.fetchSetters();
    },
    methods: {
      async fetchRoutes() {
        try {
          const response = await fetch(`${this.API_BASE_URL}/routes/`);
          if (!response.ok) throw new Error("Error fetching routes");
          this.routes = await response.json();
        } catch (err) {
          console.error(err.message);
        }
      },
      async fetchWalls() {
        try {
          const response = await fetch(`${this.API_BASE_URL}/walls/`);
          if (!response.ok) throw new Error("Error fetching walls");
          this.walls = await response.json();
        } catch (err) {
          console.error(err.message);
        }
      },
      async fetchSetters() {
        try {
          const response = await fetch(`${this.API_BASE_URL}/setters/`);
          if (!response.ok) throw new Error("Error fetching setters");
          this.setters = await response.json();
        } catch (err) {
          console.error(err.message);
        }
      },
      async submitRoute() {
        try {
          const newRoutePayload = {
            ...this.newRoute,
            style: "classic",
            status: "active",
            description: "Newly added route",
          };
          const response = await fetch(`${this.API_BASE_URL}/routes/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(newRoutePayload),
          });
          if (!response.ok) throw new Error("Failed to create route");
          // Resetta il form
          this.newRoute = {
            name: "",
            grade: "",
            color: "",
            date_set: "",
            wall_id: null,
            setter_id: null,
          };
          this.fetchRoutes();
        } catch (err) {
          console.error(err.message);
        }
      },
    },
  };
  </script>
  
  <style scoped>
@import "@/assets/styles/common.css";
.route-item {
  font-style: italic;
  transition: background-color 0.3s ease;
}

.route-item:hover {
  background-color: #f0f0f0;
}

</style>
  