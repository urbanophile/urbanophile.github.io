Title: About Me
Author: Matt Gibson
Summary:  I am a software and machine learning developer in Sydney, NSW, Australia. I like computing, data, machine learning and cooking. 
Save_as: about.html

![A bad photo of me in my darkest days]({attach}../images/me_bad.png)

<form id="contactForm" class="contact-form notice gentle-flex">
  <fieldset>
  <legend>Got an interesting question? Get in touch</legend>
  <input type="text" name="name" placeholder="Your Name" required>
  <input type="email" name="email" placeholder="Your Email" required>
  <textarea name="message" placeholder="Your Message" required></textarea>
  <button type="submit">Send Message</button>
  </fieldset>
</form>

<script>
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const formData = new FormData(this);
  
  fetch('https://script.google.com/macros/s/AKfycbxPR0yIyxn6YntmvvUvgCi8iabO586JhGdOQ6ebL5vlyuufaW37IA8GdAvZqOyEs-f2Uw/exec', {
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


I am a software and machine learning developer in [Sydney](http://en.wikipedia.org/wiki/Sydney), NSW, Australia. I like [computing](https://en.wikipedia.org/wiki/MOS_Technology_6502), [data](https://search.r-project.org/CRAN/refmans/vcd/html/HorseKicks.html), [machine learning](https://pytorch.org/) and [cooking](https://web.archive.org/web/20160210065535/http://www.seriouseats.com/the-food-lab/?ref=nav_main). I'm delighted by the scientific enterprise which allows us ["to see a World in a Grain of Sand"](https://www.poetryfoundation.org/poems/43650/auguries-of-innocence). 

I'm also quite keen on gibbons 🐒.

I acknowledge and pay my respects to Gadigal and Wangal people of the Eora nation, the Traditional Custodians of the land on which I work and live, and their elders past and present. Sovereignty was never ceded. 

## About Website 
This second version of my homepage hosted by [Github Pages](https://docs.github.com/en/pages), [CDN, DNS, and Analytics with Cloudflare](https://www.cloudflare.com/), image compression with [squoosh.app](https://squoosh.app/) and [oxiPNG](https://github.com/shssoichiro/oxipng) and created using [Pelican](https://github.com/getpelican/pelican).



