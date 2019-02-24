.. include:: /common/global.rst

Twitter: Write adaptor
======================

The Twitter Write adaptor allows the following Twitter actions to be
taken:

-  Reply to a tweet
-  Tweet a new tweet
-  Retweet a tweet
-  Send a direct message

Creating the adaptor
--------------------

Create a **Twitter** adaptor, and when it appears for configuration, in
the **Twitter Action** list, be sure to click **Write**. For information
about creating or configuring adaptors, see |adaptors|_.

.. |adaptors| replace:: \ |acquia-product:aj| \ adaptors
.. _adaptors: /journey/adaptors

After you have created the adaptor, complete the following actions:

#. In the **Twitter Write Option** section, select one of the following
   values:

   -  **Reply**
   -  **Tweet**
   -  **Retweet**
   -  **Direct Message**

#. Depending on which Twitter Write option chosen you will have to
   provide one or more other pieces of information.
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | Action    | User      | TweetId   | Tweet     | User Id   | Note      |
   |           | Screen    |           | Text      |           |           |
   |           | Name      |           |           |           |           |
   +===========+===========+===========+===========+===========+===========+
   | Reply     | Required  | Required  | Required  | Not       | Replies   |
   |           |           |           |           | Required  | must      |
   |           |           |           |           |           | start     |
   |           |           |           |           |           | with the  |
   |           |           |           |           |           | user      |
   |           |           |           |           |           | screen    |
   |           |           |           |           |           | name.     |
   |           |           |           |           |           | This is   |
   |           |           |           |           |           | pre-popul |
   |           |           |           |           |           | ated.     |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | Tweet     | Not       | Not       | Required  | Not       | Just      |
   |           | Required  | Required  |           | Required  | requires  |
   |           |           |           |           |           | the new   |
   |           |           |           |           |           | tweet     |
   |           |           |           |           |           | text      |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | Retweet   | Not       | Required  | Not       | Not       | Only      |
   |           | Required  |           | Required  | Required  | requires  |
   |           |           |           |           |           | the       |
   |           |           |           |           |           | ``id`` of |
   |           |           |           |           |           | the tweet |
   |           |           |           |           |           | that is   |
   |           |           |           |           |           | being     |
   |           |           |           |           |           | retweeted |
   +-----------+-----------+-----------+-----------+-----------+-----------+
   | Direct    | Not       | Not       | Required  | Required  | Requires  |
   | Message   | Required  | Required  |           |           | the user  |
   |           |           |           |           |           | id and    |
   |           |           |           |           |           | the       |
   |           |           |           |           |           | message   |
   |           |           |           |           |           | to be     |
   |           |           |           |           |           | sent      |
   +-----------+-----------+-----------+-----------+-----------+-----------+

#. Optionally provide an array of Twitter Media Ids. Acquia does not
   upload the media, and these must be loaded externally. These will be
   `64-bit integer
   identifiers <https://dev.twitter.com/overview/api/entities>`__.

For each of the **Reply**, **Tweet**, and **Retweet** actions, the
output from the node is the new `tweet
object <https://dev.twitter.com/overview/api/tweets>`__ that has been
created.

For the **Direct Message** action the value returned is the unique id of
the direct message.

Validation warnings
-------------------

+-----------------------------------+-----------------------------------+
| Warning                           | Description                       |
+===================================+===================================+
| **Adaptor does not have           | It is necessary to create a       |
| connection set**                  | connection and choose it from the |
|                                   | Adaptor Connection drop down      |
+-----------------------------------+-----------------------------------+
| **This adaptor's configuration    | No data location for the message  |
| requires a data source to be      | to be written to the queue has    |
| set**                             | been chosen                       |
+-----------------------------------+-----------------------------------+
