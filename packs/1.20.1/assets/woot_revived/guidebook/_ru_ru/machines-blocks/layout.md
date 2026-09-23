---
navigation:
  parent: machines-blocks/machines-blocks-index.md
  title: "Схема фабрики"
  icon: "woot_revived:layout"
---
# Схема фабрики

<BlockImage id="layout" scale="5"/>

<ItemImage id="layout" scale="0.5"/> Схема фабрики показывает вам чертеж (структуру) фабрики.

Вы можете нажать по ней ПКМ, чтобы изменить тир (уровень) отображаемой фабрики.

Все блоки в предпросмотре не имеют коллизии, неразрушимы и могут быть напрямую заменены на соответствующие им настоящие блоки.

## Крафт

<RecipeFor id="layout" />

# Предпросмотр

<Row>
  <Column>
    ## Медный

    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/layout/copper.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>
  </Column>

  <Column>
    ## Железный

    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/layout/iron.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>
  </Column>

  <Column>
    ## Золотой

    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/layout/gold.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>
  </Column>

  <Column>
    ## Алмазный

    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/layout/diamond.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>
  </Column>

  <Column>
    ## Незеритовый

    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/layout/netherite.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>
  </Column>
</Row>