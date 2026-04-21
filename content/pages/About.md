Title: About Me
Author: Matt Gibson
Summary:  I am a software and machine learning developer in Sydney, NSW, Australia. I like computing, data, machine learning and cooking. 
Save_as: about.html

![A bad photo of me in my darkest days]({attach}../images/me_bad.png)

<form class="notice gentle-flex" aria-label="Contact form"
      data-ajax
      data-success-msg="✓ Message sent!"
      data-error-msg="✗ Something went wrong — try emailing me directly.">
  <fieldset>
    <legend>Got an interesting question? Get in touch</legend>
    <input type="text" name="website" autocomplete="off" tabindex="-1" aria-hidden="true" style="display:none" />
    <input type="hidden" name="formType" value="contact" />
    <input type="hidden" name="formLoadTime" />
    <label for="contactName">Name</label>
    <input type="text" id="contactName" name="name" placeholder="Ellen Ripley" required />
    <label for="contactEmail">Email</label>
    <input type="email" id="contactEmail" name="email" placeholder="eripley@nostromo.com" required />
    <label for="contactMessage">Message</label>
    <textarea id="contactMessage" name="message" placeholder="Your message" required></textarea>
    <button type="submit">Send Message</button>
  </fieldset>
  <div class="form-message" role="status" aria-live="polite"></div>
</form>
<p class="form-spam-count">{{ SPAM_COUNT }} spam submissions caught</p>


I am a software and machine learning developer in [Sydney](http://en.wikipedia.org/wiki/Sydney), NSW, Australia. I like [computing](https://en.wikipedia.org/wiki/MOS_Technology_6502), [data](https://search.r-project.org/CRAN/refmans/vcd/html/HorseKicks.html), [machine learning](https://pytorch.org/) and [cooking](https://web.archive.org/web/20160210065535/http://www.seriouseats.com/the-food-lab/?ref=nav_main). I'm delighted by the scientific enterprise which allows us ["to see a World in a Grain of Sand"](https://www.poetryfoundation.org/poems/43650/auguries-of-innocence). 

I'm also quite keen on gibbons 🐒.

I acknowledge and pay my respects to Gadigal and Wangal people of the Eora nation, the Traditional Custodians of the land on which I work and live, and their elders past and present. Sovereignty was never ceded. 

## About Website 
This second version of my homepage hosted by [Github Pages](https://docs.github.com/en/pages), [CDN, DNS, and Analytics with Cloudflare](https://www.cloudflare.com/), image compression with [squoosh.app](https://squoosh.app/) and [oxiPNG](https://github.com/shssoichiro/oxipng) and created using [Pelican](https://github.com/getpelican/pelican).



