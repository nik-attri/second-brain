---
author: Shoaib Akhtar
fetched_at: '2026-10-04T08:58:41.113323Z'
id: b92235a71e2e
lane: lead
published: ''
source: linkedin
title: '⚙️ .NET Backend Development Series — Day 14


  "Include()" — Getting Related Data in EF Core


  While working with EF Core,'
url: https://www.linkedin.com/posts/shoaib-akhtar-3519bb2b0_dotnet-aspnetcore-efcore-activity-7512422547833978880-URMM
---

⚙️ .NET Backend Development Series — Day 14

"Include()" — Getting Related Data in EF Core

While working with EF Core, I reached a point where I didn't just need the booking.

I also needed to know which customer made that booking.

That's where "Include()" becomes really useful.

🏨 Simple Example

Suppose we have:

Customer → Bookings

If I only do:

var bookings = await db.Bookings
    .ToListAsync();

I get the bookings, but the related customer data isn't automatically loaded.

With "Include()":

var bookings = await db.Bookings
    .Include(x => x.Customer)
    .ToListAsync();

Now EF Core also loads the related "Customer" for each booking.

So I can access:

booking.Customer.Name

🔗 Why is this useful?

Imagine an API response like:

Booking
 ├── Guest Name
 ├── Nights
 ├── Total Amount
 └── Customer
      ├── Name
      └── Email

Instead of manually writing separate queries, "Include()" lets EF Core load the related navigation property as part of the query.

💡 Something important I learned

"Include()" is useful, but I shouldn't use it everywhere just because I can.

If an API only needs a few fields, projection with "Select()" can often be a better choice than loading a large object graph.

So I'm keeping this simple rule in mind:

Need the related entity? → "Include()"

Need only specific fields? → Consider "Select()"

The more I work with EF Core, the more I realize that writing the query is only half the job.

Understanding what data I'm actually asking the database to return is just as important.

What do you prefer for API responses: "Include()" or "Select()"?

#DotNet #ASPNetCore #EFCore #EntityFrameworkCore #CSharp #BackendDevelopment #WebAPI #SoftwareEngineering #Database #100DaysOfCode
