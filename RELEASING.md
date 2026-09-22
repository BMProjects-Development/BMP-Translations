# Releasing BMP Translations

Full documentation is available in
[English](docs/GUIDE_EN.md) and [Russian](docs/GUIDE_RU.md).

Each supported Minecraft version is an independent release line. Its current
BMP Translations version is stored in `packs/<minecraft>/VERSION`.

## One-time GitHub setup

Add these repository secrets under **Settings → Secrets and variables →
Actions**:

- `CURSEFORGE_TOKEN` — an author API token allowed to upload files to the BMP
  Translations project (`1372113`).
- `MODRINTH_TOKEN` — a Modrinth token with permission to create versions for
  `bmp-translations`.

GitHub Releases use the repository-provided `GITHUB_TOKEN`; no separate GitHub
secret is needed.

## Normal release

The repository-migration commit that first introduces `packs/` should not
contain a release marker. It establishes the changelog baseline without
publishing the already released pack versions again.

1. Edit files below `packs/<minecraft>/`.
2. Increase that pack's `VERSION` using semantic versioning.
3. Commit the version change in the same final commit that contains the release
   marker. Resource changes may be in that commit or in earlier commits since
   the previous release. Put one exact marker on its own line:

   ```text
   Update 1.21.1 translations

   release all
   ```

The supported markers are:

- `release all` — GitHub, CurseForge, and Modrinth.
- `release gh` — GitHub only.
- `release cf` — CurseForge only.
- `release mr` — Modrinth only.

When several `VERSION` files change in the marked commit, every changed pack
is released independently. For example, Minecraft 1.20.1 and 1.21.1 receive
separate ZIP files, platform entries, GitHub releases, and tags.

GitHub can mark only one release as `Latest`. Each workflow run marks its newest
released Minecraft version as `Latest`. Therefore a single-version release always
becomes the latest release by date, while a multi-version release uses the highest
Minecraft version from that run.

A version-specific tag is always created, even when the marker publishes only
to CurseForge or Modrinth. The tag is the immutable changelog baseline for the
next release.

Tags use this format:

```text
mc1.21.1-v1.1.5
```

## Retrying one platform

If one platform failed after another already published successfully, create a
new commit without increasing the version and explicitly name the affected
Minecraft version:

```text
Retry CurseForge publication

release cf 1.21.1
```

Multiple versions can be separated by spaces or commas:

```text
release mr 1.20.1 1.21.1
```

Explicit version markers are intended for recovery. A normal release should
select packs by changing their `VERSION` files.

## Changelog generation

The changelog is generated from file changes since the previous tag for the
same Minecraft version. It is not generated from commit descriptions.

The English section is emitted first, followed by the Russian section. The
generator reports added, updated, and removed asset namespaces and counts
added, changed, and removed translation keys in JSON and `.lang` files.

Each generated `packs/<minecraft>/mods.json` catalog stores full project names,
the resource namespaces they cover, and optional platform links:

```json
{
  "name": "Applied Energistics 2",
  "namespaces": ["ae2"],
  "curseforge": "https://www.curseforge.com/minecraft/mc-mods/applied-energistics-2",
  "modrinth": "https://modrinth.com/mod/ae2",
  "resolved": true
}
```

After a successful release, the metadata job refreshes the catalogs, both
language-specific pack README files, the root README links, and the bilingual
Modrinth description. Uncertain matches are kept with `resolved: false` and no
invented platform link. These files are not included in the resource-pack ZIP.

## Local validation

Python 3.11 or newer is sufficient; the scripts have no third-party
dependencies.

```shell
python scripts/release_tools.py validate
python scripts/release_tools.py build --all --output dist
python scripts/mod_metadata.py sync --discover
```

The validator checks pack metadata, JSON/JSON-with-comments files, conflicting
path casing, and the required pack structure. Builds are deterministic: the
same sources produce byte-identical ZIP files.
