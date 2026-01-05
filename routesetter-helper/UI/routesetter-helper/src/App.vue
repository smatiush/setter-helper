<template>
  <v-app>
    <!-- Header con navigazione -->
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Route Setter Dashboard</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text :to="{ name: 'Walls' }">Walls</v-btn>
      <v-btn text :to="{ name: 'Routes' }">Routes</v-btn>
      <v-btn text :to="{ name: 'Explore' }">Explore</v-btn>
    </v-app-bar>

    <!-- Visualizza il contenuto della pagina corrente -->
    <router-view></router-view>

    <!-- Snackbar per errori (se necessario) -->
    <v-snackbar v-model="errorMessage" color="white" timeout="3000">
      {{ errorMessage }}
    </v-snackbar>
  </v-app>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      errorMessage: "",
    };
  },
};
</script>

<style>
@import "@/assets/styles/common.css";

/* aggiungi altri stili globali specifici per App.vue se necessario */
</style>
