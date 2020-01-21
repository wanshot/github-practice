

def test():
    """http://bp.lvh.me:8000/projects/bp/pages/9
    """
    # http://lvh.me:8000/s/3e906d8db66c49e7a5bbe5a0bd555740
    pass


パターン1 - 1行に重複する複数のURL

http://bp.lvh.me:8000/projects/bp/pages/10 http://bp.lvh.me:8000/projects/bp/pages/10

パターン2 - 1行に重複する複数のパーマリンク

http://lvh.me:8000/s/8b30c406b221448c8b995d528e6facf2 http://lvh.me:8000/s/8b30c406b221448c8b995d528e6facf2


パターン3 - 1行に重複しない複数のURL
http://bp.lvh.me:8000/projects/bp/pages/12 http://bp.lvh.me:8000/projects/bp/pages/13


パターン4 - 1行に重複しない複数のパーマリンク

http://lvh.me:8000/s/38b73ee3b1104fe2bbf236de46cbbdcf http://lvh.me:8000/s/2b9085a5b71d4c598f4a9be458bff9dc

パターン5 - URLに似た文字列

* hなし ttp://bp.lvh.me:8000/projects/bp/pages/15
* subdomainが違う http://bpp.lvh.me:8000/projects/bp/pages/15

パターン6 - パーマリンクに似た文字列

* uidが31文字 http://lvh.me:8000/s/2b9085a5b71d4c598f4a9be458bff9d
* hなし ttp://lvh.me:8000/s/2b9085a5b71d4c598f4a9be458bff9dc
* ドメインが違う http://vh.me:8000/s/2b9085a5b71d4c598f4a9be458bff9dc
