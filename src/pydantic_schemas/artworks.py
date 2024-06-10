from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Measurement(BaseModel):
    elementName: str
    elementDescription: str
    elementMeasurements: dict


class ArtWork(BaseModel):
    objectID: int
    isHighlight: bool
    accessionNumber: str
    accessionYear: str
    isPublicDomain: bool
    primaryImage: str
    primaryImageSmall: str
    additionalImages: List[str] = []
    constituents: Optional[list]
    department: str
    objectName: str
    title: str
    culture: str
    period: str
    dynasty: str
    reign: str
    portfolio: str
    artistRole: str
    artistPrefix: str
    artistDisplayName: str
    artistDisplayBio: str
    artistSuffix: str
    artistAlphaSort: str
    artistNationality: str
    artistBeginDate: str
    artistEndDate: str
    artistGender: str
    artistWikidata_URL: str
    artistULAN_URL: str
    objectDate: str
    objectBeginDate: int
    objectEndDate: int
    medium: str
    dimensions: str
    # dimensionsParsed: Optional[float | int] #узнать почему в документации есть, а по факту нет
    measurements: List[Measurement] = []
    creditLine: str
    geographyType: str
    city: str
    state: str
    county: str
    country: str
    region: str
    subregion: str
    locale: str
    locus: str
    excavation: str
    river: str
    classification: str
    rightsAndReproduction: str
    linkResource: str
    metadataDate: datetime = Field(format='%Y-%m-%dT%H:%M:%S.%fZ')
    repository: str
    objectURL: str
    tags: Optional[list]
    objectWikidata_URL: str
    isTimelineWork: bool
    GalleryNumber: str
