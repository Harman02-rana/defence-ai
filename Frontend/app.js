console.log("🔵 Predict button clicked");


async function predict() {
  const payload = {
  heart_rate: Number(heart_rate.value),
  stress_level: Number(stress_level.value),
  sleep_hours: Number(sleep_hours.value),
  fatigue_level: Number(fatigue.value),
  age: Number(age.value),
  blood_pressure: Number(blood_pressure.value),
  oxygen_level: Number(oxygen_level.value),
  daily_steps: Number(steps.value)
};


  const res = await fetch("http://127.0.0.1:8000/predict-risk", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await res.json();

  localStorage.setItem("result", JSON.stringify(data));
  location.href = "result.html";
}
