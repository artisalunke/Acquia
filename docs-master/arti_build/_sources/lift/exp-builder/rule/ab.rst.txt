.. include:: /common/global.rst

Planning your A/B testing
=========================

When you create an A/B test, it can be helpful to know approximately how
long you'll need to test your results. Although it's impossible to know
exactly how long the process will take, there are several attributes and
thresholds that you can use to get a better idea of the test's running
timeline.

.. note::  

   -  This page contains information only for A/B testing. Although you can
      use some of the information on this page for other tests, the
      estimates and guidelines it provides may not be accurate.
   -  For information about conducting A/B (split) tests with
      |journeylink|_, see `Split Test node </journey/node/ab>`__.


.. |journeylink| replace:: \ |acquia-product:aj|\ 
.. _journeylink: /journey

.. _collect:

Collecting website data
-----------------------

As an example, you want to test to see if a different banner design on
your homepage improves conversion over the existing banner design.
Before you create your test, examine your website's analytics to obtain
the following values for an average day:

-  Website visitors to your homepage
-  Website visitors that click the existing banner

For our example, if (on average) your website has 1,000 visitors and 50
visitors click the banner, you have a 5% *conversion rate*.

To determine if the new banner has better results, you'll need to set an
appropriate threshold for success. Is the new banner better than the
existing one if conversion increases to 6%, or would it only be
successful if it were over 10%? Raising conversion to 6% represents a
20% *lift* or increase in Average Differential Return (indicated by the
symbol `α - alpha <https://en.wikipedia.org/wiki/Alpha_(finance)>`__),
while raising it to 10% represents a 100% lift.

.. _calculate:

Calculating required website visitors
-------------------------------------

After you collect your website's statistics, use an online calculator_ 
to help you determine how many visitors it will take to ensure that your
A/B test results are *statistically significant*. Based on the previous
example, to see a 20% lift (6% conversion increase), your website
requires approximately 7,663 visitors per variation (or 15,326 total
visitors for the two banners). At a rate of approximately 1,000 visitors
per day, you can expect that the testing will take two weeks until you
can be sure that the success threshold is met or not.

.. _calculator: http://www.evanmiller.org/ab-testing/sample-size.html#!5;80;5;1;0

Although you can stop your A/B test before the required number of
website visitors view your banners, doing so can affect the reliability
of your results. Ensuring that your results are statistically
significant can indicate that the test's results are real values and not
a random effect.

The most common number to use for statistical significance is 95%, which
is also the default in the linked online calculator, and is represented
by an α (alpha) of 5%.

.. note::  

   This is the inverse of the 95% significance in the |acquia-product:cha|
   interface, but represents the same data.

The other percentage on the calculator page is the *statistical power*
that we want to have with this test, which indicates the percent of time
that the minimum effect size will be detected, assuming it exists. In
this calculation, that minimum effect that we want to find is the change
from a 5% conversion to a 6% conversion. You can change the percentage
to have more statistical power or more statistical significance if you
desire.
