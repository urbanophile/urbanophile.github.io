var FORMS_ENDPOINT = 'https://script.google.com/macros/s/AKfycbylMyfo6MCXTG0ULL6nctqCwmEWIx8MS4s3G0756_PH967xJShv_Nl2nz9PdaECPlA2yw/exec';

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('form[data-ajax]').forEach(function (form) {
    // set load time for bot check
    var loadTimeInput = form.querySelector('[name="formLoadTime"]');
    if (loadTimeInput) loadTimeInput.value = Date.now();

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var btn = form.querySelector('[type="submit"]');
      var msg = form.querySelector('.form-message');
      var honeypot = form.querySelector('[name="website"]');

      // honeypot check
      if (honeypot && honeypot.value) return;

      // time check
      if (loadTimeInput && Date.now() - parseInt(loadTimeInput.value) < 3000) {
        msg.textContent = '✗ Submission too fast — please try again.';
        return;
      }

      var originalLabel = btn.textContent;
      btn.disabled = true;
      btn.innerHTML = '<span class="spinner" aria-hidden="true"></span> ' + originalLabel + '…';
      msg.textContent = '';

      fetch(FORMS_ENDPOINT, { method: 'POST', body: new FormData(form) })
        .then(function () {
          msg.textContent = form.dataset.successMsg || '✓ Sent!';
          form.reset();
          if (loadTimeInput) loadTimeInput.value = Date.now();
        })
        .catch(function () {
          msg.textContent = form.dataset.errorMsg || '✗ Something went wrong — try again.';
        })
        .finally(function () {
          btn.disabled = false;
          btn.textContent = originalLabel;
        });
    });
  });
});
