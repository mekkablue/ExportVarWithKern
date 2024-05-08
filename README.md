# ExportVarWithKern

Glyphs.app plugin for exporting a variable font with an automated KERN axis (for fading out kerning). 

After installation and an app restart, choose _File > Export,_ pick the _VAR with KERN_ option in the export dialog, choose an axis tag (`KERN` recommended), and an axis name (default ‘Kerning’), click Continue and choose a destination in the upcoming Save dialog. All Variable Font Settings in _File > Font Info > Exports_ will be exported with an additional kerning axis with a range of 0 (no kerning) to 100 (fully applied kerning).

### License

Copyright 2024 Rainer Erich Scheichelbauer (@mekkablue), idea by Rob Keller (@Rob-Keller).
Based on sample code by Georg Seifert (@schriftgestalt). 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
