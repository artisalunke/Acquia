.. include:: /common/global.rst

Understanding Acquia log analysis
=================================

One of Acquia's internal monitoring tools performs a log analysis of
recent traffic to your website, allowing the Support team to determine
if there have been changes to your website's traffic patterns, or your
website's response to them, by breaking down per-hour traffic reports
into a table.

Acquia Support will sometimes provide this output to customers to help
them understand what changes took place, and when. The output file may
appear densely packed with information; this article can help you to
interpret its contents.

.. _data:

Data structure
--------------

Here's an example of what the output might look like:

``Date/Time          #Reqs   Avg(s)  Max(s)  #>5s  HTTP:2XX  3XX   4XX   403   404   5XX 28/Jul/2015:10:XX  40817   0.20    13.66   37    33413     1430  5974  690   5284  0 28/Jul/2015:11:XX  41395   0.24    47.05   125   34743     1490  5158  1168  3990  1 28/Jul/2015:12:XX  52454   0.21    13.02   82    44709     2097  5637  827   4810  9 28/Jul/2015:13:XX  60165   0.20    15.08   54    51330     2393  6439  868   5571  3 28/Jul/2015:14:XX  71464   0.23    10.43   29    62365     2997  6090  824   5266  11 28/Jul/2015:15:XX  92274   0.26    10.25   116   81635     3777  6857  889   5968  4``

In the previous list, each line represents the compilation of an hour's
requests. Every column in this line provides information about the
traffic seen in this hour.

+-----------------------------------+-----------------------------------+
| Column                            | Description                       |
+===================================+===================================+
| **#Reqs**                         | The total number of requests this |
|                                   | hour. A larger number can         |
|                                   | indicate a traffic spike.         |
+-----------------------------------+-----------------------------------+
| **Avg(s)**                        | The average, in seconds, of how   |
|                                   | long each request took to         |
|                                   | complete. A larger number would   |
|                                   | indicate an hour where your       |
|                                   | website's instances struggled to  |
|                                   | keep up with demand.              |
+-----------------------------------+-----------------------------------+
| **Max(s)**                        | The maximum number of seconds the |
|                                   | longest request took to complete  |
|                                   | in this hour.                     |
+-----------------------------------+-----------------------------------+
| **#>5s**                          | How many requests in this hour    |
|                                   | took more than five seconds to    |
|                                   | complete.                         |
+-----------------------------------+-----------------------------------+
| **HTTP:2XX**                      | The number of requests this hour  |
|                                   | that responded with a ``2XX``     |
|                                   | HTTP response code, indicating    |
|                                   | that the request was received and |
|                                   | handled successfully. Higher      |
|                                   | numbers in this column are        |
|                                   | better.                           |
+-----------------------------------+-----------------------------------+
| **3XX**                           | The number of requests this hour  |
|                                   | that responded with a ``3XX``     |
|                                   | HTTP response code, indicating a  |
|                                   | good request, but requiring some  |
|                                   | kind of redirection to complete.  |
+-----------------------------------+-----------------------------------+
| **4XX**                           | The number of requests this hour  |
|                                   | that responded with a ``4XX``     |
|                                   | HTTP response code, which         |
|                                   | typically indicates a problem     |
|                                   | (potentially client-side). Two    |
|                                   | specific ``4XX``-level response   |
|                                   | codes are are broken out          |
|                                   | separately in the following       |
|                                   | columns.                          |
+-----------------------------------+-----------------------------------+
| **403**                           | Forbidden. The request was a      |
|                                   | valid request, but the server is  |
|                                   | refusing to respond to it.        |
+-----------------------------------+-----------------------------------+
| **404**                           | Not Found. The requested resource |
|                                   | does not exist.                   |
+-----------------------------------+-----------------------------------+
| **5XX**                           | The server has encountered an     |
|                                   | error.                            |
+-----------------------------------+-----------------------------------+

For more information about HTTP status codes, see `List of HTTP status
codes <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes>`__.

.. _read:

What to look for
----------------

When reading this report, Acquia looks for many things, including:

-  Did the number of requests spike upward?
-  Did the average response time spike upward?
-  What requests take a tremendously long time to complete?
-  Did the overall ratio between ``2XX/3XX/4XX/5XX`` responses change?
-  Are there a great deal of ``5XX`` requests?
-  Does the ratio between good (``2XX`` / ``3XX``) traffic and traffic
   returning ``404`` warrant a fix to the underlying cause of the
   ``404``\ s or the usage of the `Fast
   404 <%5Bacquia-product:kb%5Darticles/using-fast-404-drupal>`__ module
   to lessen their effect?

Acquia Support will generally make recommendations and point out where
problems may be based on these statistics. By analyzing when and how the
data changed, and comparing it to events that may have taken place at
that time (such as code deploys, media campaigns, or news events), you
can use this information to help understand where you may need to look
to make optimization changes to your website.
