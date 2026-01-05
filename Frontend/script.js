async function predictRisk() {
    const data = {
        age: Number(document.getElementById("age").value),
        heart_rate: Number(document.getElementById("heartRate").value),
        stress_level: Number(document.getElementById("stress").value),
        sleep_hours: Number(document.getElementById("sleep").value),
        fatigue_level: Number(document.getElementById("fatigue").value),
        blood_pressure: Number(document.getElementById("bp").value),
        oxygen_level: Number(document.getElementById("oxygen").value),
        daily_steps: Number(document.getElementById("steps").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("result").innerHTML = `
            <h3>Risk Level: ${result.risk_level}</h3>
            <p>Risk Score: ${result.risk_score}</p>
        `;

    } catch (error) {
        document.getElementById("result").innerHTML =
            "❌ Backend not reachable.";
        console.error(error);
    }
}
