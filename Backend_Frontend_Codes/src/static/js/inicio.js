function scrollToSection(event) {
  event.preventDefault(); // Evita el envío del formulario por defecto
  
  var section = document.getElementById('we_Do');
  section.scrollIntoView({ behavior: 'smooth' });
  
  // Aquí puedes realizar cualquier otra lógica adicional antes de enviar el formulario
  event.target.submit(); // Envía el formulario manualmente
}