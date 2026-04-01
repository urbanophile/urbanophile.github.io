Title: Welcome to my homepage
Author: Matt Gibson
Summary: Experienced professional always open to opportunities. Ph.D. in Computer Vision and Machine Learning with practical experience.
Save_as: index.html
Template: homepage



👋 hi there, thanks for visiting. My name is Matt and I am a software / machine learning person in Sydney. I am an irregular blogger, this is mostly to order my thoughts.

![Detail from Anni Albers]({attach}../images/anni_albers_detail.png)


  <form id="subscriptionForm" class="notice gentle-flex" aria-label="Newsletter subscription">
    <p>Crave tepid content? Subscribe to my monthly newsletter below! <small>It's just the blog</small></p>
    <fieldset id="formCtrls">
      <legend class="sr-only">Subscribe to newsletter</legend>
      <label for="email">Email</label>
      <input id="email" name="email" type="email" autocomplete="email" placeholder="eripley@nostromo.com" required />
      <button id="submitBtn" type="submit">Subscribe</button>
    </fieldset>
    <div id="messageDiv" role="status" aria-live="polite"></div>
  </form>

<style>
.sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip: rect(0,0,0,0); white-space: nowrap; border: 0;
}
@keyframes spin { to { transform: rotate(360deg); } }
.spinner {
  display: inline-block; width: 1em; height: 1em;
  border: 2px solid currentColor; border-top-color: transparent;
  border-radius: 50%; animation: spin 0.6s linear infinite;
  vertical-align: middle;
}
</style>

<script>
document.getElementById('subscriptionForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const btn = document.getElementById('submitBtn');
  const msg = document.getElementById('messageDiv');

  btn.disabled = true;
  btn.innerHTML = '<span class="spinner" aria-hidden="true"></span> Subscribing…';
  msg.textContent = '';

  fetch('https://script.google.com/macros/s/AKfycbylMyfo6MCXTG0ULL6nctqCwmEWIx8MS4s3G0756_PH967xJShv_Nl2nz9PdaECPlA2yw/exec', {
    method: 'POST',
    body: new FormData(this)
  })
  .then(() => {
    msg.textContent = '✓ Subscribed! You\'ll hear from me next month.';
    this.reset();
  })
  .catch(() => {
    msg.textContent = '✗ Something went wrong — try again or email me directly.';
  })
  .finally(() => {
    btn.disabled = false;
    btn.textContent = 'Subscribe';
  });
});
</script>



The most recent mid content I wrote:
