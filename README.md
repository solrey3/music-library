# music-library

## File Management

I have an extremely large music library to damage.

My full collection I keep on a Windows 10 machine and use [MusicBee](https://getmusicbee.com/) to manage my collection.

I have one subset of that collection which contains select tracks on my MacBook Pro which I sync with my iPhone.

I have another subset mostly of albums on another Mac which I sync with my iPod.

Since I use iTunes on my Macs, I try to make sure my Musicbee library management mimicks iTunes utilizing the following File Organizer script:

```
$If($And(<Album Artist>="Various Artists",<iTunes Compilation>>0),Compilations,$RxReplace(<Album Artist>,"^\.|\.$","_"))\$IsNull(<Album>,"Unknown Album",$RxReplace(<Album>,"^\.|\.$","_"))\$If(<Disc Count>>1,<Disc-Track#>" ",$If($And(<Disc Count>=0,<Disc#>>0),<Disc-Track#>" ",$If(<Track#>=0,,<Track#>" ")))<Title>
```

I also run into issues with non-ASCII double-byte characters in playlists trying to get my library files to match, so I created a small python script to help replace those problematic filenames in my M3U8 playlists. On Windows, there are issues with the ☮ symbol in Prince's _Sign "☮" the Times_. For now, just take it out of the list.

I use [iTunesExport](https://www.ericdaugherty.com/dev/itunesexport/) to bring over my iTunes playlists into [MusicBee](https://getmusicbee.com/) and run the earlier mentioned Python script on those playlists.

## Adding New Music To Collection

[MusicBrainz Picard](https://picard.musicbrainz.org/) is an excellent tool to help manage tags to my new music. I am a stciker in regards to original release dates of songs, so I am hoping to utilize the APIs from [Wikidata](https://www.wikidata.org/w/api.php?action=help), [Genius](https://docs.genius.com/), and [MusicBrainz](https://musicbrainz.org/doc/Development/XML_Web_Service/Version_2) to help pull proper release dates for my collection.

