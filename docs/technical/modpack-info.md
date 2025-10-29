# Modpack Structure

Finding documentation on a Minecraft modpack is proving difficult, so I'll be
documenting what I find here.

## Links

- [Curseforge Approved Third-Party
    mods](https://docs.google.com/spreadsheets/d/176Wv-PZUo9hFxy6oC6N8tWdquBLPRtSuLbNK-r0_byM/edit#gid=0)

## Structure

Here is an example of what a modpack structure might look like:

```
modpack/
├── config/
│   ├── mod1-config.toml
│   ├── mod2-config.toml
│   └── ...
├── mods/
│   ├── mod1.jar
│   ├── mod2.jar
│   └── ...
├── scripts/
│   ├── script1.zs
│   ├── script2.zs
│   └── ...
├── resources/
│   ├── resource1.zip
│   ├── resource2.zip
│   └── ...
├── defaultconfigs/
│   ├── default1.toml
│   ├── default2.toml
│   └── ...
├── overrides/
│   ├── config/
│   │   ├── mod1-config.toml
│   │   ├── mod2-config.toml
│   │   └── ...
│   ├── defaultconfigs/
│   │   ├── default1.toml
│   │   ├── default2.toml
│   │   └── ...
│   ├── resources/
│   │   ├── resource1.zip
│   │   ├── resource2.zip
│   │   └── ...
│   ├── scripts/
│   │   ├── script1.zs
│   │   ├── script2.zs
│   │   └── ...
│   ├── server_scripts/
│   │   ├── script1.js
│   │   ├── script2.js
│   │   └── ...
│   ├── client_scripts/
│   │   ├── script1.js
│   │   ├── script2.js
│   │   └── ...
│   └── ...
└── README.md
```
