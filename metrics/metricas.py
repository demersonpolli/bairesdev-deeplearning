def acuracia(vp, vn, fp, fn):
    """Calcula a acurácia do modelo."""
    return (vp + vn) / (vp + vn + fp + fn)

def especificidade(vn, fp):
    """Calcula a especificidade do modelo."""
    return vn / (vn + fp)

def f1(vp, fp, fn):
    """Calcula o F1 Score do modelo."""
    return (2 * vp) / ((2 * vp) + fp + fn)

def precisao(vp, fp):
    """Calcula a precisão do modelo."""
    return vp / (vp + fp)

def sensibilidade(vp, fn):
    """Calcula a sensibilidade do modelo."""
    return vp / (vp + fn)

