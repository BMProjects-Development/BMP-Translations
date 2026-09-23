---
navigation:
  title: "Как захватить моба?"
  position: 20
  icon: "mob_shard"
---
# Как захватить моба?

Чтобы захватить моба, вам понадобится <ItemImage id="mob_shard" scale="0.5"/> Осколок моба.

## Как создать Осколок моба

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="assets/anvil/mob_shard.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="mob_shard" scale="2"/>
  Для его создания вам понадобятся <ItemImage id="shard_mold" scale="0.5"/> форма для осколка и 2 <ItemImage id="stygian_ingot" scale="0.5"/> Стигийских слитка.
</Row>

## Как использовать Осколок моба

Получив Осколок моба, для захвата существа вам сначала нужно ударить его этим осколком.

Вы также можете бросить осколок в моба. Когда вы бросаете осколок,
он становится неуязвимым ко всему, кроме лавы.

Если после удара по мобу осколок не перешел в состояние захвата, вероятно, этот моб находится в черном списке или не является живой сущностью.

После успешного захвата моба вам нужно убить его 5 раз любым оружием, при этом удерживая
Осколок моба в инвентаре.

После 5 убийств Осколок моба будет полностью запрограммирован, и вы сможете превратить его в <ItemImage id="fake_spawner" scale="0.5"/> Фальшивый рассадник.

## Как создать Фальшивый рассадник

Чтобы фабрика приняла ваш захват, вам нужно превратить ваш <ItemImage id="mob_shard" scale="0.5"/> Осколок моба в <ItemImage id="fake_spawner" scale="0.5"/> Фальшивый рассадник.

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="assets/anvil/fake_spawner.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="fake_spawner" scale="2"/>
  Для его создания вам понадобятся <ItemImage id="mob_shard" scale="0.5"/> Осколок моба, <ItemImage id="prism" scale="0.5"/> Призма и <ItemImage id="factory_base" scale="0.5"/> Основание фабрики.
</Row>