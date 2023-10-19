from IPython.core.magic import register_line_cell_magic

@register_line_cell_magic
def gala(line: str = None, cell: str = None):
    from ._gala import galarina
    import stackview

    if line is not None and cell is not None:
        # Syntax:
        # %%gala 5 
        # images showing rabbits
        return stackview.slice(galarina(prompt=cell, num_images = int(line)))
    if line is not None and cell is None:
        # Syntax: 
        # %gala image showing rabbit
        return stackview.insight(galarina(prompt=line))
    if line is None and cell is not None:
        # Syntax:
        # %%gala
        # an image showing a rabbit
        return stackview.insight(galarina(prompt=cell))
    