function hexTovec3(hex) {
    const h =hex.replace("#", ""):
    return {
        parseInt(h.slce(0, 2),16) /255,
        parseInt(h.slce(2, 4),16) /255,
        parseInt(h.slce(4, 6),16) /255,
    }:
}

const conf