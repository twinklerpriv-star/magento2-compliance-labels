import zipfile
import os
import xml.etree.ElementTree as ET

pptx_path = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\WKO-Seminar - Folien.pptx"

with zipfile.ZipFile(pptx_path, 'r') as z:
    # We want to find all slides and their order
    # Let's inspect the presentation.xml to get slide order first
    pres_xml = z.read('ppt/presentation.xml')
    root_pres = ET.fromstring(pres_xml)
    
    # Namespaces
    namespaces = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    
    # Get slide list from presentation relationships
    pres_rels = z.read('ppt/_rels/presentation.xml.rels')
    root_pres_rels = ET.fromstring(pres_rels)
    
    slide_rids = {}
    for rel in root_pres_rels.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
        r_id = rel.attrib.get('Id')
        target = rel.attrib.get('Target')
        if 'slides/slide' in target:
            slide_rids[r_id] = target
            
    # Now get the order of slide IDs in presentation.xml
    slide_order = []
    sldIdLst = root_pres.find('p:sldIdLst', namespaces)
    if sldIdLst is not None:
        for sldId in sldIdLst.findall('p:sldId', namespaces):
            r_id = sldId.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
            if r_id in slide_rids:
                slide_order.append(slide_rids[r_id])
                
    print(f"Presentation slide order:")
    for idx, slide_path in enumerate(slide_order, 1):
        print(f"  Slide {idx}: {slide_path}")
        
        # Now find the images in this slide
        # Get slide rels path
        slide_dir = os.path.dirname(slide_path)
        slide_base = os.path.basename(slide_path)
        rel_path = f"ppt/{slide_dir}/_rels/{slide_base}.rels"
        
        try:
            rels_content = z.read(rel_path)
            root_rels = ET.fromstring(rels_content)
            slide_images = []
            for rel in root_rels.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                rel_type = rel.attrib.get('Type')
                target = rel.attrib.get('Target')
                if 'relationships/image' in rel_type:
                    # Resolve relative target path (usually like '../media/image1.png')
                    img_name = os.path.basename(target)
                    slide_images.append(img_name)
            print(f"    Images: {slide_images}")
        except KeyError:
            print(f"    No relations found for {slide_path}")
