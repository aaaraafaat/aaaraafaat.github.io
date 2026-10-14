"""Builds the static pages of aaaraafaat.github.io from the content below.

Edit the text here, run `python build.py`, then commit and push.
Writing rules: short sentences, no dashes as punctuation, nothing about ADT or AceVector yet.
"""
from pathlib import Path

ROOT = Path(__file__).parent
NAME = "Abu Jehad Arafat"
NAV = [("index.html", "About"), ("publications.html", "Publications"),
       ("projects.html", "Projects"), ("teaching.html", "Teaching"), ("files/Arafat_CV.pdf", "CV")]

SIDE = """<aside class="side">
  <img src="images/profile.jpg" alt="Abu Jehad Arafat" width="200" height="253">
  <h1>Abu Jehad Arafat</h1>
  <p class="role">M.Sc. Data Science and Machine Learning. Flying instructor and former fighter pilot.</p>
  <ul>
    <li>Dhaka, Bangladesh</li>
    <li><a href="mailto:aaaraafaat@outlook.com">aaaraafaat@outlook.com</a></li>
    <li><a href="https://linkedin.com/in/aaaraafaat">LinkedIn</a></li>
    <li><a href="https://github.com/aaaraafaat">GitHub</a></li>
    <li><a href="files/Arafat_CV.pdf">CV (PDF)</a></li>
  </ul>
</aside>"""


def page(file, title, body):
    nav = "\n    ".join(
        f'<a href="{href}"{" class=\"on\"" if href == file else ""}>{label}</a>' for href, label in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="Abu Jehad Arafat: robust machine perception and safe autonomy. Former fighter pilot and flying instructor, M.Sc. in Data Science and Machine Learning.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="topbar">
  <nav>
    <a class="home" href="index.html">{NAME}</a>
    {nav}
  </nav>
</header>
<div class="wrap">
{SIDE}
<main>
{body}
</main>
</div>
<footer><div>&copy; 2026 {NAME}. All images on this site show my own work and use synthetic or illustrative data. Nothing here represents the position of any other organisation.</div></footer>
</body>
</html>
"""
    (ROOT / file).write_text(html, encoding="utf-8")


ABOUT = """<section>
<h2>About me</h2>
<p>I study machine perception that has to keep working when its input degrades, and autonomous systems that must act safely when it does not.</p>
<p>I flew for seventeen years in the Bangladesh Air Force as a fighter pilot and flying instructor. Much of that time was spent in poor weather, and much of the teaching was about one skill: knowing when a sense has stopped being reliable and changing to one that still is. I now want to build that skill into machines.</p>
<p>In September 2026 I completed an M.Sc. in Data Science and Machine Learning at State University of Bangladesh with a CGPA of 4.00 out of 4.00. My thesis tested whether a free, training-free fog score can warn an object detector that an image is hard. On real fog it cannot be trusted in one direction, and the paper reports that negative result in full.</p>
<p>I also served as a United Nations aviation safety officer in Darfur and taught Air Law and Airmanship as adjunct university faculty. Today I manage simulation and training-technology projects for the Air Force.</p>
<p>I am looking for a PhD position starting in Fall 2027 in robust perception, uncertainty and safe autonomy, with aerial robots as the first test case.</p>
</section>

<section>
<h2>Research interests</h2>
<ul>
<li>Robust perception in degraded visual environments: fog, rain and low light.</li>
<li>Knowing when perception fails: calibrated confidence and failure detection for detectors.</li>
<li>Safe decisions after a failure: slow down, switch sensors or hand control to a person.</li>
<li>Simulation and human-in-the-loop training for safety-critical systems.</li>
</ul>
</section>

<section>
<h2>News</h2>
<ul class="news">
<li><span class="d">Sep 2026</span><span>Completed the M.Sc. in Data Science and Machine Learning, State University of Bangladesh, CGPA 4.00 / 4.00.</span></li>
<li><span class="d">2026</span><span>Thesis paper under review at <i>IEEE Transactions on Intelligent Vehicles</i>.</span></li>
<li><span class="d">2026</span><span>Released the thesis <a href="https://github.com/aaaraafaat/perception-difficulty-dve">code and figures</a>.</span></li>
<li><span class="d">2024&ndash;25</span><span>Led a PC-based aviation training device project, from hardware selection to fielded use.</span></li>
<li><span class="d">2023</span><span>Postgraduate Diploma in Aviation Instruction, Bangladesh University of Professionals.</span></li>
<li><span class="d">2016</span><span>Staff Officer, Aviation Safety, United Nations mission in Darfur (UNAMID).</span></li>
</ul>
</section>"""

PUBS = """<section>
<h2>Publications</h2>
<h3>Under review</h3>
<div class="pub">
<div>A. J. Arafat and P. C. Shil.</div>
<div class="t">Dark-Channel Fog Severity as a Safety Signal: Failure Modes and Limits on Real Fog.</div>
<div><i>IEEE Transactions on Intelligent Vehicles</i>, under review, 2026.</div>
<div class="meta"><a href="https://github.com/aaaraafaat/perception-difficulty-dve">Code and figures</a></div>
</div>
</section>

<section>
<h2>Thesis</h2>
<p class="t"><b>Perception-Difficulty Estimation in Degraded Visual Environments</b></p>
<p class="meta">M.Sc. thesis, State University of Bangladesh, 2026. Supervisor: Prof. Pintu Chandra Shil.</p>
<p>Can a free, training-free physics score tell a camera-based vehicle when fog is degrading its object detector? I calibrated the dark-channel fog severity score on 2,000 synthetic-fog images and tested it on real fog (RTTS, 4,245 images) against three clear-trained detectors: YOLO-nano, YOLOv8-S and RT-DETR-L.</p>
<ul>
<li>Where the score reports a near-clear image, <b>39.9%</b> of images are still detection failures.</li>
<li>The best of 11 appearance descriptors separates them from truly clear scenes at only <b>AUC 0.686</b>.</li>
<li>A second free estimator, the colour attenuation prior, shares the same blind spot on ordinary grey daylight fog.</li>
</ul>
<p><b>Takeaway:</b> trust a high score, never a low one.</p>
</section>"""

PROJECTS = """<section>
<h2>Projects</h2>
<p>Training and simulation systems built for the Air Force. All images use synthetic or illustrative data.</p>

<h3>PC-based aviation training device</h3>
<p class="meta">2024&ndash;2025 &middot; Project lead</p>
<div class="shots"><img src="images/pcatd-01.png" alt="Training device, exterior view" loading="lazy"><img src="images/pcatd-02.png" alt="Training device, cockpit" loading="lazy"></div>
<p>A training device built from commercial hardware on Prepar3D and MSFS with a custom fixed-wing model, for ab-initio and part-task training. I researched and bought the hardware, designed the layout and took it to fielded use.</p>

<h3>Flying operations scheduling and progress monitoring</h3>
<p class="meta">2025&ndash;2026</p>
<div class="shots"><img src="images/ops-01.png" alt="Schedule builder" loading="lazy"><img src="images/ops-02.png" alt="Progress monitor" loading="lazy"><img src="images/ops-03.png" alt="Syllabus tracking" loading="lazy"></div>
<p>A rule-based web app that builds daily flying schedules against aircraft, instructor and trainee limits, and tracks each trainee through the syllabus.</p>

<h3>Wargame planning platform</h3>
<p class="meta">2026 &middot; Built with AI-assisted development</p>
<div class="shots"><img src="images/wargame-planner-01.png" alt="Mission type selection" loading="lazy"><img src="images/wargame-planner-02.png" alt="Target, weapon and squadron tasking panel" loading="lazy"></div>
<p>A web application for planning air missions in an exercise. Weapon and effect options are ranked by the number of aircraft each would cost. Aircraft to task are computed from squadron serviceability, assurance level and expected losses.</p>

<h3>Flight planning tool</h3>
<p class="meta">2019 &middot; Project manager and UI designer</p>
<div class="shots"><img src="images/mission-planner.png" alt="Mission route and navigation chart output" loading="lazy"></div>
<p>Google Maps API with layered custom charts, for preparing mission routes and navigation charts.</p>

<h3>VR combat simulator</h3>
<p class="meta">2018</p>
<div class="shots"><img src="images/vr-01.png" alt="VR simulator rig" loading="lazy"><img src="images/vr-02.png" alt="VR simulator in use" loading="lazy"></div>
<p>Delivered the concept for a VR part-task trainer, and later advised on the build of a VR-based training device for combat training.</p>
</section>"""

TEACHING = """<section>
<h2>Teaching</h2>

<h3>Flying instructor</h3>
<p class="meta">Flying Instructors' School and BAF Academy &middot; 2021&ndash;2025</p>
<p>In-flight and ground instruction for 65 cadet pilots and 26 instructor pilots, with assessments, check rides and technical briefings. Lectured Air Law and Instructional Technique to the 64th Flying Instructors' Course.</p>

<h3>Adjunct faculty</h3>
<p class="meta">2023&ndash;2025</p>
<ul>
<li>Air Law, Postgraduate Diploma in Aviation Instruction (3 semesters).</li>
<li>Airmanship, B.Sc. in Aeronautics (2 semesters).</li>
</ul>

<h3>Aviation safety trainer</h3>
<p class="meta">United Nations mission in Darfur (UNAMID) &middot; 2016</p>
<p>Induction training in aviation safety for more than 500 mission personnel. Wrote the e-learning content.</p>
</section>"""

if __name__ == "__main__":
    page("index.html", NAME, ABOUT)
    page("publications.html", f"Publications | {NAME}", PUBS)
    page("projects.html", f"Projects | {NAME}", PROJECTS)
    page("teaching.html", f"Teaching | {NAME}", TEACHING)
    print("built 4 pages")
