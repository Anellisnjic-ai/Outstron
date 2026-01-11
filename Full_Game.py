<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loading Screen Game</title>
    <style>
        body {
            margin: 0;
            height: 100vh;
            background: #0a0a0a;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            color: #ffffff;
        }
        #loader {
            font-size: 4rem;
            text-align: center;
        }
        #percent {
            font-size: 6rem;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div id="loader">
    <div id="text">Loading</div>
    <div id="percent">0%</div>
</div>

<script>
    let percent = 0;
    const percentEl = document.getElementById("percent");
    const textEl = document.getElementById("text");

    const interval = setInterval(() => {
        percent++;

        // When we hit 99%
        if (percent === 99) {
            textEl.textContent = "Outstron";
            percentEl.textContent = "99%";
        } else {
            percentEl.textContent = percent + "%";
        }

        // At 100% finish
        if (percent >= 100) {
            clearInterval(interval);
            setTimeout(() => {
                textEl.textContent = "Done";
                percentEl.style.display = "none";
            }, 500); // small delay for effect
        }
    }, 50); // speed of loading (50ms per percent)
</script>

</body>
</html>
