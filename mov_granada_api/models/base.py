"""Model base."""

from pydantic import BaseModel, ConfigDict


class BusGranadaAPIBaseModel(BaseModel):
    """
    Base model for Bus Granada API.

    Encapsulates common configuration for all models
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="ignore",
        exclude_unset=True,
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )
