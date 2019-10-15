<html dir="ltr" lang="en-US"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  
  <title>Thug Life Report</title>

  <meta name="description" content="At HallOfFame, we take security issues seriously. If you believe you’ve detected a vulnerability within our products we’d like to hear about it.">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

  <!-- Entypo pictograms by Daniel Bruce — www.entypo.com -->
  <link rel="stylesheet" media="all" href="sec-application.css" id="stylesheet">
  <link rel="stylesheet" type="text/css" href="sec-style.css">
  <link rel="shortcut icon" type="image/x-icon" href="HallOfFame-logo.svg">
 
  
  <!-- add code here that should appear in the document head -->

<script src="https://code.jquery.com/jquery-1.10.2.js"></script>  
<meta name="viewport" content="user-scalable=0, initial-scale=1.0">
  
</head>
<body class="">
  
  <header class="lang-selector" id="lang-selector">
</header>
<div class="expander">  
  <div class="wrapper-main">
    <header class="header">

      

      <div class="header-title">
      </div>

    </header>
  </div>
</div>


<div class="alert off">
  Site under construction.
</div>

  <main role="main">
    

<article>
   <header class="knowledge-page-header">
    <h1><center><b>Thug Life Vulnerability Scanner Report</center></b></h1>
    
 
  </header>
  
  <div class="clearfix"></div>
  <div class="article-column">
    <div class="article-body markdown">
      <div class="article-body markdown">
 <div class="ndas1">

<?php
$servername = "localhost";
$username = "userDB";
$password = "Passdb";
$dbname = "nmap_report";



// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


$totalData = "SELECT count(*) from nmap left join ip on ip.ip_address = ip and ip.port=nmap.port;";
$result_totaldata = mysqli_query($conn, $totalData);


$sql = "SELECT nmap.*, ip.title, ip.link from nmap LEFT JOIN ip On ip.ip_address = ip and  ip.port=nmap.port;";
$result = mysqli_query($conn, $sql);


if (mysqli_num_rows($result) > 0) {
    // output data of each row
    
    echo "<style>
        table, th, td {
          border: 1px solid black;
          border-collapse: collapse;
        }
        </style>";
        echo "<table style=\"width:100%\">";
        echo "<tr><th><center>ip</center></th><th><center>port</th><th><center>service</th><th><center>product</th><th><center>version</th><th><center>Title</th><th><center>Link</th></tr>";
    while($row = mysqli_fetch_assoc($result)) {
        
        echo "<tr><td>" . $row["ip"]. "</td><td>" . $row["port"]. "</td><td>" . $row["service"]."</td><td>" . $row["product"]."</td><td>" . $row["version"] ."</td><td>" . $row["title"]."</td><td><a href=\"" . $row["link"]. "\"target=\"_blank\">". $row["link"]."</td></tr>";
        
    }
    echo "</table>";
} else {
    echo "0 results";
}

mysqli_close($conn);




?>


</div>
</div>
    </div>  
  </div>
</div>
  <div class="clearfix"></div>  
  

</article>
</main>
<br>
<br>
<br>
<br>
<footer><center><img src="" width="200" height="50"/><br>
<font color="grey" size="2"><a href="#">Thug Life Report</a></font></center></footer>




