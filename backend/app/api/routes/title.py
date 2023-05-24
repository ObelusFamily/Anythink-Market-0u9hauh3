from fastapi import APIRouter, Depends

from app.api.dependencies.database import get_repository
from app.db.repositories.tags import TagsRepository
from app.models.schemas.tags import TagsInList

router = APIRouter()


@router.get("", response_model=TitleInList, name="titles:get-all")
async def get_all_titles(
    titles_repo: TitlesRepository = Depends(get_repository(TitlesRepository)),
) -> TitlesInList:
    titles = await titles_repo.get_all_titles()
    return TitlesInList(titles=titles)
