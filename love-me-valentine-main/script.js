const questionContainer = document.querySelector(".question-container");
const resultContainer = document.querySelector(".result-container");
const gifResult = document.querySelector(".gif-result");
const heartLoader = document.querySelector(".cssload-main");
const yesBtn = document.querySelector(".js-yes-btn");
const noBtn = document.querySelector(".js-no-btn");
const heartsContainer = document.getElementById("hearts-container");
const nicknameContainer = document.querySelector(".nickname-container");
const proposeBtn = document.querySelector(".js-propose-btn");
const nicknameInput = document.getElementById("nickname-input");
const finalText = document.getElementById("final-text");
const nicknameBtns = document.querySelectorAll(".nickname-btn");

// Nickname button click handlers
nicknameBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    const selectedNickname = btn.getAttribute("data-nickname");
    proceedWithNickname(selectedNickname);
  });
});

// Function to proceed with the selected/typed nickname
function proceedWithNickname(nickname) {
  nicknameContainer.style.display = "none";
  heartLoader.style.display = "block";
  stopGlitterHearts();

  setTimeout(() => {
    heartLoader.style.display = "none";
    resultContainer.style.display = "block";
    finalText.innerText = `I love you kuttypila!! As always.. ❤️`;
    gifResult.play();
  }, 2000);
}

// Change the position of no button
noBtn.addEventListener("mouseover", () => {
  const btnRect = noBtn.getBoundingClientRect();
  const maxWidth = window.innerWidth - btnRect.width;
  const maxHeight = window.innerHeight - btnRect.height;

  const newX = Math.floor(Math.random() * maxWidth);
  const newY = Math.floor(Math.random() * maxHeight);

  noBtn.style.position = "fixed";
  noBtn.style.left = `${newX}px`;
  noBtn.style.top = `${newY}px`;
});

// Yes button functionality
yesBtn.addEventListener("click", () => {
  questionContainer.style.display = "none";
  heartLoader.style.display = "block";

  setTimeout(() => {
    heartLoader.style.display = "none";
    nicknameContainer.style.display = "flex";
    startGlitterHearts();
  }, 3000);
});

// Propose button functionality (manual input)
proposeBtn.addEventListener("click", () => {
  const nickname = nicknameInput.value.trim() || "Kuttypila";
  proceedWithNickname(nickname);
});

// Background Heart Generator
function createHeart() {
  const heart = document.createElement("div");
  heart.classList.add("heart");
  const startLeft = Math.random() * 100;
  const duration = Math.random() * 3 + 3;
  const size = Math.random() * 20 + 10;

  heart.style.left = `${startLeft}vw`;
  heart.style.animationDuration = `${duration}s`;
  heart.style.width = `${size}px`;
  heart.style.height = `${size}px`;

  const colors = ["rgba(255, 105, 180, 0.7)", "rgba(255, 0, 0, 0.6)", "rgba(255, 192, 203, 0.8)"];
  heart.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

  heartsContainer.appendChild(heart);
  setTimeout(() => heart.remove(), duration * 1000);
}

// Glitter Hearts Logic
let glitterInterval;
function createGlitterHeart() {
  const glitter = document.createElement("div");
  glitter.classList.add("glitter-heart");
  glitter.style.left = Math.random() * 100 + "vw";
  glitter.style.top = Math.random() * 100 + "vh";
  glitter.style.animationDelay = Math.random() * 2 + "s";
  document.body.appendChild(glitter);
  setTimeout(() => glitter.remove(), 3000);
}

function startGlitterHearts() {
  glitterInterval = setInterval(createGlitterHeart, 150);
}

function stopGlitterHearts() {
  clearInterval(glitterInterval);
}

setInterval(createHeart, 300);
