<template>
    <v-container>
      <v-card outlined>
        <v-card-title class="headline">Walls</v-card-title>
        <v-card-text>
        <v-list-item v-for="wall in walls" :key="wall.wall_id">
            <v-list-item-title>
                {{ wall.name }} - {{ wall.location }} ({{ wall.wall_type }})
            </v-list-item-title>
        </v-list-item>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-title>Add a New Wall</v-card-title>
        <v-card-text>
          <v-form ref="wallForm" @submit.prevent="submitWall">
            <v-text-field
              label="Wall Name"
              v-model="newWall.name"
              required
            ></v-text-field>
            <v-text-field
              label="Location"
              v-model="newWall.location"
              required
            ></v-text-field>
            <v-select
              label="Type"
              v-model="newWall.wall_type"
              :items="wallTypes"
              required
            ></v-select>
            <v-btn color="primary" type="submit">Add Wall</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    name: "WallsPage",
    data() {
      return {
        API_BASE_URL: "http://localhost:8000/api",
        walls: [],
        wallTypes: ["slab", "vertical", "overhang"],
        newWall: {
          name: "",
          location: "",
          wall_type: "slab",
        },
      };
    },
    created() {
      this.fetchWalls();
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
      async submitWall() {
        try {
          const response = await fetch(`${this.API_BASE_URL}/walls/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.newWall),
          });
          if (!response.ok) throw new Error("Failed to create wall");
          // Resetta il form
          this.newWall = { name: "", location: "", wall_type: "slab" };
          this.fetchWalls();
        } catch (err) {
          console.error(err.message);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  @import "@/assets/styles/common.css";

  .wall-item:hover {
    background-color: #e0e0e0;
  }
  </style>
  