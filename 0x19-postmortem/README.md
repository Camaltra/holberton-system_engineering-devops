<h1>PostMortem</h1>

<h2>Sumary Issue</h2>

<p>
  Between 14h34 and 14h47 GTM+2, on the 12th of may 2022, a big part, 68% of our
  users (the sub-one), face a problem, they can't have access to their maps to
  see where they are. As a GPS society, that was a big bug.</br>
  The root cause of this missfunctionnement was an typo error on the API url after
  a big changement, passing from the v1.12.17 to the v2.0.0
</p>

<h2>TimeLine</h2>

<p>
    14h34 - The code was put in production three minutes ago, some user dowload the new version.</br>
    14h35 - We recieve Users feedback on twitter, due to they can't access anymore to the map.</br>
    14h39 - After call everybody on the team, we decide to investigate in all folder to see what can be wrong, listen to log of servers.</br>
    14h43 - We see a mistake in the const on the API_URL variable, gooogle was wrote, execpt that google got only two O.</br>
    14h43 - Hell no, an user send us a picture, he was lost in the desert cause he can't use our application anymore, we had to make it quick</br>
    14h43 - Thommas fall in the hallway because he was so happy to discover the bug. That was really fun to see.</br>
    14H47 - EveryThing was pushed into the main repo, and put it in production. Tested and Approuved.</br>
    14H47 - Our CM made a tweet to inform that everybody can be safe on the road now.</br>
</p>

<h2>Root cause</h2>

<p>
    The cause was an mistake in the API_URL variable, that can't fetch data from the google servers.</br>
    This was undectable if we didn't use the application in details.</br>
    Thommas see it, after long minutes of works. Now he is at hospital, hope everything right for him, because he saved the app.</br>
</p>

<h2>Corrective</h2>

<p>
    The first thing was to clear the hallway, to make it safe for the next time.</br>
    Secondly, we note to make some deeper test, maybe engage QA engineer, to make sure that every single thing is tested before
    push it into prodution.</br>
    For now, we just change all of our images to push it to all servers, make the last realese.</br>
    I'm sure we will get an award to get a bug directly after pushing the new version. v2.0.0 to v2.1.0 in less than a quarter.</br>
    Hope Thommas will get back soon.</br>
</p>
