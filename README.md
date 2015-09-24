![ARDT](http://slimgr.com/images/2015/09/23/df03047928220cbabf448110abb719b7.png)

**Akamai Reflective DDoS Tool**

*Attack the origin host behind the Akamai Edge hosts and bypass the DDoS protection offered by Akamai services.*

**How it works...**

Akamai boast around 100,000 edge nodes which offer load balancing, web application firewalling, caching etc around the 

world, to ensure that minimal requests actually hit your origin web-server. However the issue with caching is that you 

cannot cache something that is non-deterministic, I.E a search result. A search request that has not been searched before 

is likely not in the cache, and will result in the Akamai edge node requesting the resource from the origin server 

itself. 

What this tool does is, provided a list of Akamai edge nodes and a valid cache missing request, produces multiple requests that hit the origin server via the Akamai edge nodes. As you can imagine, if you had 50 IP addresses under your control, sending requests at around 20 per second, with 100,000 Akamai edge node list, and a request which resulting in 10KB hitting the origin, if my calculations are correct, thats around 976MB/ps hitting the origin server, which is a hell of a lot of traffic.
