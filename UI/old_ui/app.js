

const API_BASE_URL = "http://localhost:8000/api";

// Fetch walls and populate wall list and dropdown
async function fetchWalls() {
  try {
    const response = await fetch(`${API_BASE_URL}/walls/`);
    if (!response.ok) throw new Error("Error fetching walls");
    const walls = await response.json();

    const wallList = document.getElementById("wall-list");
    const wallSelect = document.getElementById("wall-select");
    wallList.innerHTML = "";
    wallSelect.innerHTML = "";

    walls.forEach((wall) => {
      // Populate wall list
      const li = document.createElement("li");
      li.textContent = `${wall.name} - ${wall.location} (${wall.wall_type})`;
      wallList.appendChild(li);

      // Populate dropdown
      const option = document.createElement("option");
      option.value = wall.wall_id;
      option.textContent = wall.name;
      wallSelect.appendChild(option);
    });
  } catch (err) {
    showError(err.message);
  }
}

// Fetch setters and populate the setter dropdown in the route form
async function fetchSetters() {
  try {
    const response = await fetch(`${API_BASE_URL}/setters/`);
    if (!response.ok) throw new Error("Error fetching setters");
    const setters = await response.json();

    const setterSelect = document.getElementById("setter-select");
    setterSelect.innerHTML = ""; // Clear previous options

    setters.forEach((setter) => {
      const option = document.createElement("option");
      option.value = setter.setter_id;
      option.textContent = setter.username;
      setterSelect.appendChild(option);
    });
  } catch (err) {
    showError(err.message);
  }
}

// Fetch routes and populate route list
async function fetchRoutes() {
  try {
    const response = await fetch(`${API_BASE_URL}/routes/`);
    if (!response.ok) throw new Error("Error fetching routes");
    const routes = await response.json();

    const routeList = document.getElementById("route-list");
    routeList.innerHTML = "";

    routes.forEach((route) => {
      const li = document.createElement("li");
      li.textContent = `${route.name} - Grade: ${route.grade} (${route.color})`;
      routeList.appendChild(li);
    });
  } catch (err) {
    showError(err.message);
  }
}

// Handle wall form submission
document.getElementById("wall-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const wallName = document.getElementById("wall-name").value;
  const wallLocation = document.getElementById("wall-location").value;
  const wallType = document.getElementById("wall-type").value;

  const newWall = {
    name: wallName,
    location: wallLocation,
    wall_type: wallType
  };

  try {
    const response = await fetch(`${API_BASE_URL}/walls/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newWall),
    });
    if (!response.ok) throw new Error("Failed to create wall");
    document.getElementById("wall-form").reset();
    fetchWalls(); // Refresh walls data
  } catch (err) {
    showError(err.message);
  }
});

// Handle route form submission
document.getElementById("route-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const routeName = document.getElementById("route-name").value;
  const routeGrade = document.getElementById("route-grade").value;
  const routeColor = document.getElementById("route-color").value;
  const routeDate = document.getElementById("route-date").value;
  const wallId = document.getElementById("wall-select").value;
  const setterId = document.getElementById("setter-select").value;

  const newRoute = {
    name: routeName,
    grade: routeGrade,
    color: routeColor,
    date_set: routeDate,
    style: "classic",
    wall_id: parseInt(wallId),
    setter_id: parseInt(setterId),
    status: "active",
    description: "Newly added route"
  };

  try {
    const response = await fetch(`${API_BASE_URL}/routes/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newRoute),
    });
    if (!response.ok) throw new Error("Failed to create route");
    document.getElementById("route-form").reset();
    fetchRoutes(); // Refresh routes data
  } catch (err) {
    showError(err.message);
  }
});

// Function to display error messages
function showError(message) {
  document.getElementById("error-message").textContent = message;
}

// Initialize by fetching walls, setters, and routes
fetchWalls();
fetchSetters();
fetchRoutes();
