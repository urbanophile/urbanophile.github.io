Title: Welcome to my homepage
Author: Matt Gibson
Summary: Experienced professional always open to opportunities. Ph.D. in Computer Vision and Machine Learning with practical experience.
Save_as: index.html
Template: homepage



👋 hi there, thanks for visiting. My name is Matt and I am a software / machine learning person in Sydney. I am an irregular blogger, this is mostly to order my thoughts. 

![Detail from Anni Albers]({attach}../images/anni_albers_detail.png)


  <form id="subscriptionForm" class="notice gentle-flex" >
  <p>Crave tepid content? Subscribe to my monthly newsletter below! <small>It's just the blog</small></p>
    <fieldset id="formCtrls">
      <label style="display:inline" for="email">Email</label>
        <input id="email" name="email" type="email" autocomplete="email" placeholder="eripley@nostromo.com" required />
      <button value="Submit" type="submit" >Submit</button>
    </fieldset>
      <div id="messageDiv"></div>
  </form>


<script>
document.getElementById('subscriptionForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const formData = new FormData(this);
  
  fetch('https://script.google.com/macros/s/AKfycbylMyfo6MCXTG0ULL6nctqCwmEWIx8MS4s3G0756_PH967xJShv_Nl2nz9PdaECPlA2yw/exec', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    alert('Message sent successfully!');
    this.reset();
  })
  .catch(error => {
    alert('Error sending message');
  });
});
</script>



The most recent mid content I wrote: 
