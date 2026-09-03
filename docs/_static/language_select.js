document.querySelectorAll("#language-selector").forEach((sel) => {
  sel.addEventListener("change", (e) => {
    window.location.href = e.target.value;
  });
});
