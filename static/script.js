const classesList = document.getElementById("classes-list");
const bookingForm = document.getElementById("booking-form");
const messageDiv = document.getElementById("message");

async function loadClasses() {
  classesList.innerHTML = "<li>Loading classes...</li>";
  try {
    const res = await fetch("/classes");
    const classes = await res.json();
    if (classes.length === 0) {
      classesList.innerHTML = "<li>No classes available</li>";
      return;
    }
    classesList.innerHTML = "";
    classes.forEach(c => {
      const li = document.createElement("li");
      const dateStr = new Date(c.datetime).toLocaleString();
      li.textContent = `ID: ${c.id} | ${c.name} with ${c.instructor} at ${dateStr} | Slots left: ${c.available_slots}`;
      classesList.appendChild(li);
    });
  } catch (error) {
    classesList.innerHTML = "<li>Error loading classes</li>";
    console.error(error);
  }
}

bookingForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  messageDiv.textContent = "";

  const data = {
    class_id: Number(bookingForm.class_id.value),
    client_name: bookingForm.client_name.value.trim(),
    client_email: bookingForm.client_email.value.trim(),
  };

  try {
    const res = await fetch("/book", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    if (!res.ok) {
      const error = await res.json();
      throw new Error(error.detail || "Booking failed");
    }

    const booking = await res.json();
    messageDiv.style.color = "green";
    messageDiv.textContent = `✅ Successfully booked class ID ${booking.class_id} for ${booking.client_name}.`;
    bookingForm.reset();
    loadClasses();
  } catch (error) {
    messageDiv.style.color = "red";
    messageDiv.textContent = `❌ ${error.message}`;
  }
});

window.onload = loadClasses;
