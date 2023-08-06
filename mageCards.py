from card import Card

'''Commands to use (No spaces before the = sign)
[Card_Name] = Card('Card Name')
[Card_Name].getsBuiltFrom([Card_Name])
'''
# Examples (I did the first few for you)

#Common Cards
Ethereal_Shield = Card("Ethereal Shield")

Magic_Bolt = Card("Magic Bolt")

#Uncommon Cards
Brutal_Thaw = Card("Brutal Thaw")

Cold_Arm = Card("Cold Arm")
Cold_Arm.getsBuiltFrom(Ethereal_Shield)

Comet_Rune = Card("Comet Rune")
Comet_Rune.getsBuiltFrom(Magic_Bolt)

Crowdsource = Card("Crowdsource")

Echo_Rune = Card("Echo Rune")

Erudition = Card("Erudition")
Erudition.getsBuiltFrom(Ethereal_Shield)

Fractal_Whip = Card("Fractal Whip")

Grimoire = Card("Grimoire")

Hellfire_Rune = Card("Hellfire Rune")

Kugi = Card("Kugi")

Lightning = Card("Lightning")

Link = Card("Link")

Meditation = Card("Meditation")

Obsidian_Dust = Card("Obsidian Dust")

Sucker_Bolt = Card("Sucker Bolt")
Sucker_Bolt.getsBuiltFrom(Magic_Bolt)

Swell = Card("Swell")

Teleport = Card("Teleport")

Unpack_the_Bag = Card("Unpack the Bag")
Unpack_the_Bag.getsBuiltFrom(Ethereal_Shield)

Unstoppable_Force = Card("Unstoppable Force")

Volcanic_Lightning = Card("Volcanic Lightning")
Volcanic_Lightning.getsBuiltFrom(Magic_Bolt)

#Rare Cards
Armageddon = Card("Armageddon")
Armageddon.getsBuiltFrom(Obsidian_Dust)
Armageddon.getsBuiltFrom(Unstoppable_Force)

Ascendance = Card("Ascendance")
Ascendance.getsBuiltFrom(Grimoire)
Ascendance.getsBuiltFrom(Link)
Ascendance.getsBuiltFrom(Unpack_the_Bag)

Bat_Bolt = Card("Bat Bolt")
Bat_Bolt.getsBuiltFrom(Sucker_Bolt)
Bat_Bolt.getsBuiltFrom(Fractal_Whip)

Blood_Surge = Card("Blood Surge")
Blood_Surge.getsBuiltFrom(Sucker_Bolt)
Blood_Surge.getsBuiltFrom(Fractal_Whip)
Blood_Surge.getsBuiltFrom(Volcanic_Lightning)


Bolt_Dance = Card("Bolt Dance")
Bolt_Dance.getsBuiltFrom(Obsidian_Dust)
Bolt_Dance.getsBuiltFrom(Brutal_Thaw)

Bolt_the_Bolted = Card("Bolt the Bolted")
Bolt_the_Bolted.getsBuiltFrom(Kugi)
Bolt_the_Bolted.getsBuiltFrom(Teleport)

Cheat = Card("Cheat")
Cheat.getsBuiltFrom(Unpack_the_Bag)

Chilly_Blow = Card("Chilly Blow")
Chilly_Blow.getsBuiltFrom(Teleport)
Chilly_Blow.getsBuiltFrom(Cold_Arm)

Conduit_Aura = Card("Conduit Aura")
Conduit_Aura.getsBuiltFrom(Swell)

Enchant = Card("Enchant")
Enchant.getsBuiltFrom(Unstoppable_Force)
Enchant.getsBuiltFrom(Meditation)

Equilibrium = Card("Equilibrium")
Equilibrium.getsBuiltFrom(Link)

Flux = Card("Flux")
Flux.getsBuiltFrom(Unstoppable_Force)

Harpoon_Bolt = Card("Harpoon Bolt")
Harpoon_Bolt.getsBuiltFrom(Volcanic_Lightning)
Harpoon_Bolt.getsBuiltFrom(Sucker_Bolt)
Harpoon_Bolt.getsBuiltFrom(Fractal_Whip)

Ice_Fort = Card("Ice Fort")
Ice_Fort.getsBuiltFrom(Cold_Arm)

Incantation = Card("Incantation")

Inferno = Card("Inferno")
Inferno.getsBuiltFrom(Hellfire_Rune)

Iron_Will = Card("Iron will")
Iron_Will.getsBuiltFrom(Erudition)

Magic_Marker = Card("Magic Marker")
Magic_Marker.getsBuiltFrom(Kugi)

Mana_Shield = Card("Mana Shield")
Mana_Shield.getsBuiltFrom(Erudition)

Mend_Wounds = Card("Mend Wounds")
Mend_Wounds.getsBuiltFrom(Swell)

Mental_Wall = Card("Mental Wall")
Mental_Wall.getsBuiltFrom(Erudition)

Meteor_Strike = Card("Meteor Strike")
Meteor_Strike.getsBuiltFrom(Echo_Rune)
Meteor_Strike.getsBuiltFrom(Crowdsource)
Meteor_Strike.getsBuiltFrom(Comet_Rune)

Mindset = Card("Mindset")
Mindset.getsBuiltFrom(Swell)

Nova = Card("Nova")
Nova.getsBuiltFrom(Volcanic_Lightning)
Nova.getsBuiltFrom(Crowdsource)

Power_is_Knowledge = Card("Power is Knowledge")

Reforge_Weakness = Card("Reforge Weakness")
Reforge_Weakness.getsBuiltFrom(Lightning)
Reforge_Weakness.getsBuiltFrom(Echo_Rune)

Reinvigorate = Card("Reinvigorate")
Reinvigorate.getsBuiltFrom(Meditation)

Rewrite = Card("Rewrite")
Rewrite.getsBuiltFrom(Grimoire)
Rewrite.getsBuiltFrom(Unpack_the_Bag)

Rune_of_Ice = Card("Rune of Ice")
Rune_of_Ice.getsBuiltFrom(Hellfire_Rune)
Rune_of_Ice.getsBuiltFrom(Comet_Rune)
Rune_of_Ice.getsBuiltFrom(Echo_Rune)

Rune_of_Thunder = Card("Rune of Thunder")
Rune_of_Thunder.getsBuiltFrom(Hellfire_Rune)
Rune_of_Thunder.getsBuiltFrom(Lightning)
Rune_of_Thunder.getsBuiltFrom(Comet_Rune)

Shuffle = Card("Shuffle")
Shuffle.getsBuiltFrom(Link)
Shuffle.getsBuiltFrom(Grimoire)

Snowball = Card("Snowball")
Snowball.getsBuiltFrom(Brutal_Thaw)

Sweep = Card("Sweep")
Sweep.getsBuiltFrom(Teleport)
Sweep.getsBuiltFrom(Cold_Arm)

Switcheroo = Card("Switcheroo")

Thriftiness = Card("Thriftiness")
Thriftiness.getsBuiltFrom(Brutal_Thaw)
Thriftiness.getsBuiltFrom(Obsidian_Dust)

Zap = Card("Zap")
Zap.getsBuiltFrom(Lightning)
Zap.getsBuiltFrom(Crowdsource)

#Legendary Cards

Aether_Splash = Card("Aether Splash")
Aether_Splash.getsBuiltFrom(Switcheroo)
Aether_Splash.getsBuiltFrom(Power_is_Knowledge)
Aether_Splash.getsBuiltFrom(Snowball)


Anamnesis = Card("Anamnesis")
Anamnesis.getsBuiltFrom(Mend_Wounds)

Arcane_Wager = Card("Arcane Wager")
Arcane_Wager.getsBuiltFrom(Magic_Marker)
Arcane_Wager.getsBuiltFrom(Ascendance)

Bolt_Hell = Card("Bolt Hell")
Bolt_Hell.getsBuiltFrom(Bat_Bolt)
Bolt_Hell.getsBuiltFrom(Meteor_Strike)
Bolt_Hell.getsBuiltFrom(Harpoon_Bolt)

Bookmark = Card("Bookmark")
Bookmark.getsBuiltFrom(Enchant)
Bookmark.getsBuiltFrom(Flux)
Bookmark.getsBuiltFrom(Mindset)
Bookmark.getsBuiltFrom(Reinvigorate)

Botaoshi = Card("Botaoshi")
Botaoshi.getsBuiltFrom(Sweep)
Botaoshi.getsBuiltFrom(Chilly_Blow)
Botaoshi.getsBuiltFrom(Bolt_the_Bolted)

Brand_of_Doom = Card("Brand of Doom")
Brand_of_Doom.getsBuiltFrom(Magic_Marker)

Channel_Pain = Card("Channel Pain")
Channel_Pain.getsBuiltFrom(Blood_Surge)
Channel_Pain.getsBuiltFrom(Reforge_Weakness)

Chaos_Rune = Card("Chaos Rune")
Chaos_Rune.getsBuiltFrom(Rune_of_Ice)
Chaos_Rune.getsBuiltFrom(Rune_of_Thunder)

Dark_Pact = Card("Dark Pact")
Dark_Pact.getsBuiltFrom(Mend_Wounds)
Dark_Pact.getsBuiltFrom(Conduit_Aura)
Dark_Pact.getsBuiltFrom(Armageddon)

Eternal_Winter = Card("Eternal Winter")
Eternal_Winter.getsBuiltFrom(Sweep)
Eternal_Winter.getsBuiltFrom(Ice_Fort)
Eternal_Winter.getsBuiltFrom(Chilly_Blow)

Ethereal_Return = Card("Ethereal Return")
Ethereal_Return.getsBuiltFrom(Zap)
Ethereal_Return.getsBuiltFrom(Meteor_Strike)

Excession = Card("Excession")
Excession.getsBuiltFrom(Ascendance)
Excession.getsBuiltFrom(Rewrite)
Excession.getsBuiltFrom(Shuffle)

Feedback_Loop = Card("Feedback Loop")
Feedback_Loop.getsBuiltFrom(Conduit_Aura)

Gallstones = Card("Gallstones")
Gallstones.getsBuiltFrom(Shuffle)
Gallstones.getsBuiltFrom(Mental_Wall)
Gallstones.getsBuiltFrom(Mana_Shield)

Glass_Shrike = Card("Glass Shrike")
Glass_Shrike.getsBuiltFrom(Reforge_Weakness)
Glass_Shrike.getsBuiltFrom(Bat_Bolt)

Grit = Card ("Grit")
Grit.getsBuiltFrom(Mindset)
Grit.getsBuiltFrom(Bolt_Dance)
Grit.getsBuiltFrom(Conduit_Aura)

Hearteater_Bolt = Card("Hearteater Bolt")
Hearteater_Bolt.getsBuiltFrom(Harpoon_Bolt)
Hearteater_Bolt.getsBuiltFrom(Bat_Bolt)

Infuse = Card("Infuse")
Infuse.getsBuiltFrom(Equilibrium)
Infuse.getsBuiltFrom(Cheat)

Midnight_Oil = Card("Midnight Oil")
Midnight_Oil.getsBuiltFrom(Thriftiness)
Midnight_Oil.getsBuiltFrom(Flux)
Midnight_Oil.getsBuiltFrom(Reinvigorate)

Mimic = Card("Mimic")
Mimic.getsBuiltFrom(Mental_Wall)
Mimic.getsBuiltFrom(Ice_Fort)
Mimic.getsBuiltFrom(Mana_Shield)

Occult_Ritual = Card("Occult Ritual")
Occult_Ritual.getsBuiltFrom(Switcheroo)
Occult_Ritual.getsBuiltFrom(Armageddon)
Occult_Ritual.getsBuiltFrom(Enchant)

Ostracon = Card("Ostracon")
Ostracon.getsBuiltFrom(Blood_Surge)
Ostracon.getsBuiltFrom(Inferno)

Outburst = Card("Outburst")
Outburst.getsBuiltFrom(Inferno)
Outburst.getsBuiltFrom(Nova)

Outside_the_Box = Card("Outside the Box")
Outside_the_Box.getsBuiltFrom(Meteor_Strike)
Outside_the_Box.getsBuiltFrom(Blood_Surge)


Paper_Library = Card("Paper Library")
Paper_Library.getsBuiltFrom(Incantation)
Paper_Library.getsBuiltFrom(Rewrite)

Paper_Recycle = Card("Paper Recycle")
Paper_Recycle.getsBuiltFrom(Power_is_Knowledge)
Paper_Recycle.getsBuiltFrom(Snowball)
Paper_Recycle.getsBuiltFrom(Switcheroo)
Paper_Recycle.getsBuiltFrom(Thriftiness)

Purify = Card("Purify")
Purify.getsBuiltFrom(Mental_Wall)

Shatter = Card("Shatter")
Shatter.getsBuiltFrom(Inferno)
Shatter.getsBuiltFrom(Rune_of_Ice)

Simulacrum = Card("Simulacrum")
Simulacrum.getsBuiltFrom(Mana_Shield)
Simulacrum.getsBuiltFrom(Iron_Will)

Subzero = Card("Subzero")
Subzero.getsBuiltFrom(Bolt_Dance)
Subzero.getsBuiltFrom(Snowball)
Subzero.getsBuiltFrom(Power_is_Knowledge)

Sunray_Rune = Card("Sunray Rune")
Sunray_Rune.getsBuiltFrom(Zap)
Sunray_Rune.getsBuiltFrom(Nova)
Sunray_Rune.getsBuiltFrom(Rune_of_Ice)

Triage = Card("Triage")

Vitruvian_Mage = Card("Vitruvian Mage")
Vitruvian_Mage.getsBuiltFrom(Rune_of_Thunder)
Vitruvian_Mage.getsBuiltFrom(Nova)
Vitruvian_Mage.getsBuiltFrom(Reforge_Weakness)

Weave_Laylines = Card("Weave Laylines")
Weave_Laylines.getsBuiltFrom(Equilibrium)
Weave_Laylines.getsBuiltFrom(Ascendance)
Weave_Laylines.getsBuiltFrom(Cheat)

Wind_Blast = Card("Wind Blast")
Wind_Blast.getsBuiltFrom(Zap)
Wind_Blast.getsBuiltFrom(Harpoon_Bolt)
Wind_Blast.getsBuiltFrom(Rune_of_Thunder)