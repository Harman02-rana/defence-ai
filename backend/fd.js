fetch("http://127.0.0.1:8000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    features: [1.2, 0.5, 3.1, 2.0]
  })
})
.then(res => res.json())
.then(data => {
  console.log("Prediction:", data.prediction);
});
