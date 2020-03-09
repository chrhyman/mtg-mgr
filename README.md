# mtg-mgr
A manager for several Magic: the Gathering concepts

# Features
- [x] Card class
  - [ ] str() handling
  - [ ] scryfall refs
  - [ ] handling multiple faces
- [x] Face class
  - [ ] str() handling
  - [ ] ability management
- [x] Cost class
  - [x] process cost string into object data
  - [ ] str() handling
  - [x] .cmc()
  - [ ] print mana cost in readable format separate from str()
- [x] Color class
  - [x] Attributes for each color individually
  - [x] Processing for informative attributes such as `monocolored` and `colorless`
  - [x] `.update()` method that re-configures all attributes and allows for partial updating of base five attributes (WUBRG)
  - [x] Handles 2-color combos (guilds)
  - [ ] Handles 3-color combos (wedges and shards)
  - [ ] Handles 4-color combos (with naming convention options)
  - [x] Attribute for when all 5 colors are present, `fivecolor`
- [ ] Some amount of implementation of Planechase
  - [ ] Having an inventory of card texts and having a plane card object that can be used
  - [ ] combined vs individual decks
  - [ ] ability to interact with digital cards like the rules would have you do (like rearranging and putting back on top and so on)
  - [ ] some sort of representation maybe image uri or just textual
