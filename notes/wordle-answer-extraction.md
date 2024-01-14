# Scraping wordle answers:

Goto: `https://wordfinder.yourdictionary.com/wordle/answers/`

Open console and inject jQuery:

```
var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);
```

Wait for script to be loaded and test with:

```
jQuery.noConflict();
```

Generate answers with:

```
jQuery("table.w-full > tbody > tr > td.rounded-r-2.px-4.py-3.font-bold:last-child:not(:has(button))").text().replaceAll('\t',"").match(/.{0,5}/g).reverse().join("");
```
