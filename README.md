<h1>Web Scraping Program</h1>
<br>
<h2>By Keanu Valencia</h2>
<br>
<h3>Description</h3>
<p>This program allows you to scrape product name and price data from the Costco and Foodland website.</p>
<br>
<h3>How To</h3>
<p>To use this program, you have to call the scrape_data() function as pass four parameters:</p>
<ol>
  <li>The webpage URL.</li>
  <li>The HTML name tag.</li>
  <li>The HTML name class.</li>
  <li>The HTML price tag.</li>
  <li>The HTML price class.</li>
</ol>
<br>
<h3>Example</h3>
<p>For the Costco webpage, you need to obtain the URL, product name tag and class, and price tag and class by inspecting the HTML code.</p>
<br>
<P>Once you have that information, you can call the scrape_data() function and pass those values as parameters. See the code below:</P>
<br>
<p>scrape_data(url="https://www.costco.com/diet-nutrition.html", name_tag="span", name_class="description", price_tag="div", price_class="price")</p>
<br>
<h3>Limitations</h3>
<p>Some product name and price data may be loaded dynamically using JavaScript. The packages used in this program (Requests and BeautifulSoup) cannot execute JavaScipt. Therefore, the program will fail to retrieve dynamically loaded data.</p>
<br>
<p>In addition, this program can only scrape data from one webpage at a time (Pagination). Therefore, the program will fail to retrieve data from multiple webpages.</p>
<br>
<h3>Improvements</h3>
<p>To over come these liminations, I will expand the program to use Selenium. Selenium is a package that automates a web browser to load JavaScript and flip to the next page or load more data.</p>
<br>
