var anagramList = [
    "Le astro piano",
    "Epsilon Aorta",
    "Re: Pita saloon",
    "Oriental soap",
    "Aeropolistan",
    "Anti-solar Poe",
    "Se&ntilde;orita Opal",
    "Paolo Stearin",
    "An oat spoiler",
    "Leo, Noa's tapir",
    "Real as potion",
    "Tao-pain? Loser...",
    "I, Satan looper",
    "No Atari slope",
    "Riot espa&ntilde;ola",
    "Airplane soot",
    "Poor Saint Ale",
    "Toenail's porn",
    "To Palaeornis!",
    "Anita, spooler",
    "I.R.A., so polenta...",
    "Arion, apostle",
    "A positron ale",
    "Rosa antipole",
    "Pale orations",
    "Ontario leaps",
    "Satin or paleo?",
    "Snort a leipoa",
    "Iron at El Paso",
    "Atop Rosaline",
    "Orleans patio",
    "Stolen aporia",
    "Aerosol paint",
    "It's near a pool",
    "Looser pi&ntilde;ata",
    "Soil near a top",
    "Arise, platoon!",
    "Tonsorial ape",
    "TIAs on parole",
    "A lotion rapes",
    "Isolator pane",
    "Teaspoon rail",
    "Alas, no pie rot",
    "Opiate Larson",
    "Loon parasite",
    "Anal isotrope",
    "Rapist on alo&euml;",
    "Tailor's paeon",
    "Personal at I/O",
    "Ion astro plea",
    "Ain't Oreos, pal!",
    "L.A. senior trap",
    "An Oslo pirate",
    "A Nepali torso",
    "No air postale",
    "O, alien pastor!",
    "Sort an ape oil"
]

function newAnagram() {
    var randomNumber = Math.floor(Math.random() * (anagramList.length));
    document.getElementById('anagramDisplay').innerHTML = anagramList[randomNumber];
}