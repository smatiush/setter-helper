<template>
  <v-container>
    <v-card outlined>
      <v-card-title class="headline">Explore</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12" md="4">
            <v-select
              v-model="selectedGrade"
              :items="gradeOptions"
              label="Filter by Grade"
              clearable
            ></v-select>
          </v-col>
          <v-col cols="12" md="4">
            <v-select
              v-model="selectedWall"
              :items="wallOptions"
              label="Filter by Wall"
              item-text="name"
              item-value="wall_id"
              clearable
            ></v-select>
          </v-col>
          <v-col cols="12" md="4">
            <v-select
              v-model="selectedWallType"
              :items="wallTypeOptions"
              label="Filter by Wall Type"
              clearable
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-card outlined class="mt-6">
      <v-card-title class="headline">Walls</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item v-for="wall in filteredWalls" :key="wall.wall_id">
            <v-list-item-title>
              {{ wall.name }} - {{ wall.location }} ({{ wall.wall_type }})
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>

    <v-card outlined class="mt-6">
      <v-card-title class="headline">Routes</v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item v-for="route in filteredRoutes" :key="route.route_id">
            <v-list-item-title>
              {{ route.name }} - Grade: {{ route.grade }} - Holds: {{ route.color }} -
              Wall: {{ routeWallName(route) }} ({{ routeWallType(route) }})
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: "ExplorePage",
  data() {
    return {
      API_BASE_URL: "http://localhost:8000/api",
      walls: [],
      routes: [],
      selectedGrade: null,
      selectedWall: null,
      selectedWallType: null,
    };
  },
  computed: {
    wallOptions() {
      return this.walls;
    },
    gradeOptions() {
      return [...new Set(this.routes.map((route) => route.grade))].filter(Boolean);
    },
    wallTypeOptions() {
      return [...new Set(this.walls.map((wall) => wall.wall_type))].filter(Boolean);
    },
    filteredWalls() {
      return this.walls.filter((wall) => {
        if (this.selectedWall && wall.wall_id !== this.selectedWall) {
          return false;
        }
        if (this.selectedWallType && wall.wall_type !== this.selectedWallType) {
          return false;
        }
        return true;
      });
    },
    filteredRoutes() {
      return this.routes.filter((route) => {
        if (this.selectedGrade && route.grade !== this.selectedGrade) {
          return false;
        }
        if (this.selectedWall && this.routeWallId(route) !== this.selectedWall) {
          return false;
        }
        if (this.selectedWallType && this.routeWallType(route) !== this.selectedWallType) {
          return false;
        }
        return true;
      });
    },
  },
  created() {
    this.fetchWalls();
    this.fetchRoutes();
  },
  methods: {
    async fetchWalls() {
      try {
        const response = await fetch(`${this.API_BASE_URL}/walls/`);
        if (!response.ok) throw new Error("Error fetching walls");
        this.walls = await response.json();
      } catch (err) {
        console.error(err.message);
      }
    },
    async fetchRoutes() {
      try {
        const response = await fetch(`${this.API_BASE_URL}/routes/`);
        if (!response.ok) throw new Error("Error fetching routes");
        this.routes = await response.json();
      } catch (err) {
        console.error(err.message);
      }
    },
    routeWall(route) {
      if (route.wall) {
        return route.wall;
      }
      const wallId = route.wall_id ?? route.wallId ?? route.wall;
      return this.walls.find((wall) => wall.wall_id === wallId);
    },
    routeWallId(route) {
      return route.wall?.wall_id ?? route.wall_id ?? route.wallId ?? null;
    },
    routeWallName(route) {
      return this.routeWall(route)?.name ?? "Unassigned";
    },
    routeWallType(route) {
      return this.routeWall(route)?.wall_type ?? "unknown";
    },
  },
};
</script>

<style scoped>
@import "@/assets/styles/common.css";
</style>
