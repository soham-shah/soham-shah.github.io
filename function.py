#!/usr/bin/env python
 
print "Content-type: text/html" 

print

contents = '''
<html>
	<head>
		<title>Linear by TEMPLATED</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href='http://fonts.googleapis.com/css?family=Roboto:400,100,300,700,500,900' rel='stylesheet' type='text/css'>
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-panels.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel-noscript.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-desktop.css" />
		</noscript>
	</head>
	<body>

	<!-- Header -->
		<div id="header">
			<div id="nav-wrapper"> 
				<!-- Nav -->
				<nav id="nav">
					<ul>
						<li><a href="index.html">Homepage</a></li>
						<li class="active"><a href="function.html">Function</a></li>
					</ul>
				</nav>
			</div>
			<div class="container"> 
				
				<!-- Logo -->
				<div id="logo">
					<h1><a href="#">Stock Insights</a></h1>
				</div>
			</div>
		</div>
	<!-- Header --> 

	<!-- Main -->
		<div id="main">
			<div class="container">
				<div class="row">

					<!-- Sidebar -->
					
					
					<!-- Content -->
					<div id="content" class="8u skel-cell-important">
						<section>
							<header>
								<h2>Function</h2>
								<span class="byline">AAPL CSV (4 Rows)</span>
							</header>
							<style type="text/css">
							.tg  {border-collapse:collapse;border-spacing:5;}
							.tg td{font-family:Arial, sans-serif;font-size:14px;padding:15px 10px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
							.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:5px 10px;border-style:solid;border-width:3px;overflow:hidden;word-break:normal;}
							.tg .tg-yw4l{vertical-align:center}
							</style>
							<table class="tg">
							  <tr>
							    <th class="tg-yw4l">date</th>
							    <th class="tg-yw4l">close</th>
							    <th class="tg-yw4l">volume</th>
							    <th class="tg-yw4l">open</th>
							    <th class="tg-yw4l">high</th>
							    <th class="tg-yw4l">low</th>
							  </tr>
							  <tr>
							    <td class="tg-yw4l">16:00</td>
							    <td class="tg-yw4l">110.78</td>
							    <td class="tg-yw4l">51,984,855</td>
							    <td class="tg-yw4l">109.85</td>
							    <td class="tg-yw4l">111.3698</td>
							    <td class="tg-yw4l">109.07</td>
							  </tr>
							  <tr>
							    <td class="tg-yw4l">10/2/15</td>
							    <td class="tg-yw4l">110.38</td>
							    <td class="tg-yw4l">57774940</td>
							    <td class="tg-yw4l">108.01</td>
							    <td class="tg-yw4l">111.0136</td>
							    <td class="tg-yw4l">107.55</td>
							  </tr>
							  <tr>
							    <td class="tg-yw4l">10/1/15</td>
							    <td class="tg-yw4l">109.58</td>
							    <td class="tg-yw4l">63849470</td>
							    <td class="tg-yw4l">109.07</td>
							    <td class="tg-yw4l">109.62</td>
							    <td class="tg-yw4l">107.31</td>
							  </tr>
							  <tr>
							    <td class="tg-yw4l">9/30/15</td>
							    <td class="tg-yw4l">110.3</td>
							    <td class="tg-yw4l">66300930</td>
							    <td class="tg-yw4l">110.17</td>
							    <td class="tg-yw4l">111.54</td>
							    <td class="tg-yw4l">108.73</td>
							  </tr>
							</table>
						</section>
					</div>

				</div>
			</div>
		</div>
	<!-- /Main -->

	<!-- Tweet -->
		<div id="tweet">
			<div class="container">
				<section>
					<blockquote>&ldquo;Insert Quote here.&rdquo;</blockquote>
				</section>
			</div>
		</div>
	<!-- /Tweet -->

	<!-- Footer -->
		<div id="footer">
			<div class="container">
				<section>
					<header>
						<h2>Get in touch</h2>
						<span class="byline">Social Media Plugs</span>
					</header>
					<ul class="contact">
						<li><a href="#" class="fa fa-twitter"><span>Twitter</span></a></li>
						<li class="active"><a href="#" class="fa fa-facebook"><span>Facebook</span></a></li>
						<li><a href="#" class="fa fa-dribbble"><span>Pinterest</span></a></li>
						<li><a href="#" class="fa fa-tumblr"><span>Google+</span></a></li>
					</ul>
				</section>
			</div>
		</div>
	<!-- /Footer -->

	<!-- Copyright -->
		<div id="copyright">
			<div class="container">
				Design: <a href="http://templated.co">TEMPLATED</a> Images: <a href="http://unsplash.com">Unsplash</a> (<a href="http://unsplash.com/cc0">CC0</a>)
			</div>
		</div>


	</body>
</html>
'''

print contents