![ARDT](http://i.imgur.com/IQycZsc.png)

**Akamai Reflective DDoS Tool**

*Attack the origin host behind the Akamai Edge hosts and bypass the DDoS protection offered by Akamai services.*

**How it works...**

*Based off the research done at NCC:*  (https://dl.packetstormsecurity.net/papers/attack/the_pentesters_guide_to_akamai.pdf)

Akamai boast around 100,000 edge nodes around the world which offer load balancing, web application firewall, caching etc, to ensure that a minimal amount of requests actually hit your origin web-server beign protected. However, the issue with caching is that you cannot cache something that is non-deterministic, I.E a search result. A search that has not been requested before is likely not in the cache, and will result in a Cache-Miss, and the Akamai edge node requesting the resource from the origin server itself. 

What this tool does is, provided a list of Akamai edge nodes and a valid cache missing request, produces multiple requests that hit the origin server via the Akamai edge nodes. As you can imagine, if you had 50 IP addresses under your control, sending requests at around 20 per second, with 100,000 Akamai edge node list, and a request which resulting in 10KB hitting the origin, if my calculations are correct, thats around 976MB/ps hitting the origin server, which is a hell of a lot of traffic.

**Finding Akamai Edge Nodes**

To find Akamai Edge Nodes, the following script has been included:

```# python ARDT_Akamai_EdgeNode_Finder.py```

This can be edited quite easily to find more, it then saves the IPS automatically.
