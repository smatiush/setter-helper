<template>
  <v-container>
    <v-card outlined class="mb-6">
      <v-card-title class="headline">Explore</v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12" md="4">
            <v-select
              label="Filter by Grade"
              v-model="filters.grade"
              :items="gradeOptions"
              clearable
            ></v-select>
          </v-col>
          <v-col cols="12" md="4">
            <v-select
              label="Filter by Wall"
              v-model="filters.wallId"
              :items="wallOptions"
              item-text="name"
              item-value="wall_id"
              clearable
            ></v-select>
          </v-col>
          <v-col cols="12" md="4">
            <v-select
              label="Filter by Wall Type"
              v-model="filters.wallType"
              :items="wallTypeOptions"
              clearable
            ></v-select>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <v-row>
      <v-col cols="12" md="5">
        <v-card outlined>
          <v-card-title class="headline">Walls</v-card-title>
          <v-card-text>
            <v-list v-if="filteredWalls.length">
              <v-list-item v-for="wall in filteredWalls" :key="wall.wall_id">
                <v-list-item-title>
                  {{ wall.name }} - {{ wall.location }} ({{ wall.wall_type }})
                </v-list-item-title>
              </v-list-item>
            </v-list>
            <div v-else class="empty-state">No walls match the current filters.</div>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" md="7">
        <v-card outlined>
          <v-card-title class="headline">Routes</v-card-title>
          <v-card-text>
            <v-list v-if="filteredRoutes.length">
              <v-list-item v-for="route in filteredRoutes" :key="route.id || route.route_id">
                <v-list-item-title>
                  {{ route.name || 'Route' }} · Grade {{ route.grade }} ·
                  {{ getWallLabel(route) }}
                  <span v-if="getWallType(route)">({{ getWallType(route) }})</span>
                </v-list-item-title>
                <v-list-item-subtitle>
                  Holds color: {{ route.color }} · Setter: {{ route.setter_id }}
                </v-list-item-subtitle>
              </v-list-item>
            </v-list>
            <div v-else class="empty-state">No routes match the current filters.</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "ExplorePage",
  data() {
    return {
      API_BASE_URL: "http://localhost:8000/api",
      routes: [],
      walls: [],
      filters: {
        grade: null,
        wallId: null,
        wallType: null,
      },
    };
  },
  computed: {
    gradeOptions() {
      const grades = this.routes
        .map((route) => route.grade)
        .filter((grade) => grade !== undefined && grade !== null && grade !== "");
      return [...new Set(grades)].sort();
    },
    wallOptions() {
      return this.walls;
    },
    wallTypeOptions() {
      const types = this.walls
        .map((wall) => wall.wall_type)
        .filter((type) => type);
      return [...new Set(types)].sort();
    },
    wallById() {
      return this.walls.reduce((acc, wall) => {
        acc[wall.wall_id] = wall;
        return acc;
      }, {});
    },
    wallByName() {
      return this.walls.reduce((acc, wall) => {
        acc[wall.name] = wall;
        return acc;
      }, {});
    },
    filteredWalls() {
      return this.walls.filter((wall) => {
        const matchesWall = this.filters.wallId
          ? wall.wall_id === this.filters.wallId
          : true;
        const matchesType = this.filters.wallType
          ? wall.wall_type === this.filters.wallType
          : true;
        return matchesWall && matchesType;
      });
    },
    filteredRoutes() {
      return this.routes.filter((route) => {
        const routeWall = this.resolveWall(route);
        const matchesGrade = this.filters.grade
          ? route.grade === this.filters.grade
          : true;
        const matchesWall = this.filters.wallId
          ? routeWall && routeWall.wall_id === this.filters.wallId
          : true;
        const matchesType = this.filters.wallType
          ? routeWall && routeWall.wall_type === this.filters.wallType
          : true;
        return matchesGrade && matchesWall && matchesType;
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
    resolveWall(route) {
      if (!route) return null;
      const directId = route.wall_id || route.wallId || route.wall?.wall_id || route.wall?.id;
      if (directId && this.wallById[directId]) {
        return this.wallById[directId];
      }
      if (typeof route.walls === "string" && this.wallByName[route.walls]) {
        return this.wallByName[route.walls];
      }
      if (route.wall && this.wallByName[route.wall]) {
        return this.wallByName[route.wall];
      }
      return null;
    },
    getWallLabel(route) {
      const wall = this.resolveWall(route);
      return wall ? `${wall.name} · ${wall.location}` : route.walls || "Unknown wall";
    },
    getWallType(route) {
      const wall = this.resolveWall(route);
      return wall ? wall.wall_type : "";
    },
  },
};
</script>

<style scoped>
@import "@/assets/styles/common.css";

.empty-state {
  color: #757575;
  font-style: italic;
  padding: 8px 0;
}
</style>
