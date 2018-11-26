var anagramList = [
    "Le astro piano",
    "Epsilon Aorta",
    "Pirate saloon",
    "Oriental soap",
    "Aeropolistan",
    "Anti-solar Poe",
    "Se&ntilde;orita Opal",
    "Paolo Stearin",
    "An oat spoiler",
    "Leo, Noa's tapir",
    "Real as potion",
    "Tao loser pain",
    "I, Satan looper",
    "No Atari slope",
    "Riot espa&ntilde;ola",
    "Airplane soot",
    "Poor Saint Ale",
    "Toenail's porn",
]

function newAnagram() {
    var randomNumber = Math.floor(Math.random() * (anagramList.length));
    document.getElementById('anagramDisplay').innerHTML = anagramList[randomNumber];
}
