---
author: Cody Croslow
fetched_at: '2026-11-15T10:09:20.905275Z'
id: f16c20aaf85c
lane: lead
published: ''
source: linkedin
title: "Anyone want to nerd out on their homelab setups? I'll go first! \nDocker infrastructure,\
  \ running on a little i3 box sitti"
url: https://www.linkedin.com/posts/codycroslow_anyone-want-to-nerd-out-on-their-homelab-activity-7527662574457372672-erOl
---

Anyone want to nerd out on their homelab setups? I'll go first! 
Docker infrastructure, running on a little i3 box sitting in my 'server' closet.

The main anchor container and general driving force of my homelab is Home Assistant. 

There are many like it, but this one is mine. 

I use HA to automate/digitize almost every switch in my house, my HVAC controls, washer and dryer timing, and have dashboards for my other homelab containers (see below).

I use mainly zwave and zigbee protocols/devices because I like them, and they're fast, and totally local. They can be a little hit or miss based on brand, but in general, I'm a fan, and I tend to lean into zwave, though I secretly think zigbee is better. 

I'm also running n8n locally for automations and workflows. 

I have containers to manage my containers, a maria database running for HA historical storage, node red, because I have adhd and can't decide on a workflow manager (plus n8n came out later with cool integrations with HA), I run zwavejs2mqtt because it works better than the native integration, plus.... mqtt... grafana + influxdb for visualizations, some tracking/uptime containers... 

Lately (as in the past few days), I've been working on self-hosting a family management tool so our family can manage all of our family things... Calendars, chores, events, recipes, even journaling. I'm using kinwall, and plan on having it running on a detachable tablet in the kitchen, but still need to wire up MCP between HA and kinwall, and then n8n<>kinwall so that I can mimic the way skylight does the whole "email to recipe and grocery list" functions. 

I took this project on NOT because there aren't great products out there (skylight), but because I wanted to own all of it, have total control, and be able to use it even without wifi. 

Anyway. I'm interested in hearing what others are doing in their homelabs.
