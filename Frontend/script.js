async function predictRisk() {
    const fatigue = document.getElementById("fatigue").value;
    const sleep = document.getElementById("sleep").value;
    const stress = document.getElementById("stress").value;
    const mission = document.getElementById("mission").value;

    const response = await fetch("http://127.0.0.1:8000/predict-risk", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            fatigue: Number(fatigue),
            sleep: Number(sleep),
            stress: Number(stress),
            mission_intensity: Number(mission)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `⚠️ Risk Level: <b>${data.risk_level}</b>`;
}
