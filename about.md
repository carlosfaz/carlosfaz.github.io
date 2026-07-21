---
layout: page
title: Sobre mí
permalink: /about/
---

<div class="svg-container">
    <img src="{{ site.baseurl }}/new-aboutme.svg" alt="Sobre mí">
</div>

<style>
.svg-container {
    display: flex;
    justify-content: center;
    padding: 20px 0;
    
    /* Truco para romper el margen del contenedor padre */
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
}

.svg-container img {
    /* Ajusta este porcentaje si quieres que ocupe menos o más del ancho de la pantalla */
    width: 90%; 
    max-width: 1200px; /* Un límite opcional para que no sea absurdamente gigante en monitores 4K */
    height: auto;
    display: block;
}
</style>
