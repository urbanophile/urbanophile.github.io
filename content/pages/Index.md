Title: Welcome to my homepage
Author: Matt Gibson
Summary: Experienced professional always open to opportunities. Ph.D. in Computer Vision and Machine Learning with practical experience.
Save_as: index.html
Template: homepage



👋 hi there, thanks for visiting. My name is Matt and I am a software / machine learning person in Sydney. I am an irregular blogger, this is mostly to order my thoughts. 

![Detail from Anni Albers]({attach}../images/anni_albers_detail.png)


  <form id="subscribeInfo" class="notice" >
  <p>Crave tepid content? Subscribe to my monthly newsletter below! <small>It's just the blog</small></p>
    <fieldset id="formCtrls">
      <label for="email">Email</label>
        <input id="email" name="email" type="email" autocomplete="email" placeholder="eripley@nostromo.com" required />
      <button value="Submit" type="submit" >Submit</button>
    </fieldset>
      <div id="messageDiv"></div>
  </form>

<script>
const form = document.querySelector("#subscribeInfo");
const messageDiv = document.querySelector("#messageDiv");
const formCtrls = document.querySelector("#formCtrls");
async function sendData() {
  // Associate the FormData object with the form element
  const formData = new FormData(form);
  formCtrls.setAttribute("disabled", "disabled")
  messageDiv.innerHTML = "Sending...";
  try {
    const response = await fetch('https://contact-list-api.matthew-gibson.workers.dev/submit', {
      method: "POST",
      // Set the FormData instance as the request body
      body: formData,
    });
    console.log("fetch response", await response.json());
    if (response.ok) {
      console.log("response ok", response);
      messageDiv.innerHTML = "Thanks for subscribing!";
      formCtrls.style.display = "none";
    } else {
      console.log("response bad", response.status);

      messageDiv.innerHTML = "Uh oh, something went wrong with request, maybe shoot me an email? ";

    }
  } catch (e) {
    console.error(e);
    messageDiv.innerHTML = "Uh oh, something went wrong!";
  }
}

// Take over form submission
form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendData();
});
</script>


The most recent mid content I wrote: 
