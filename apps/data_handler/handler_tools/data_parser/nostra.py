"""
This module contains the logic to parse the nostra data to human-readable format.
"""
from typing import Any
from data_handler.handler_tools.data_parser.serializers import (
    DebtMintEventData,
    DebtBurnEventData,
    BearingCollateralMintEventData,
    BearingCollateralBurnEventData
)


class NostraDataParser:
    """
    Parses the nostra data to human-readable format.
    """
    def parse_interest_rate_model_event(self):
        pass

    def parse_non_interest_bearing_collateral_mint_event(self):
        pass

    def parse_non_interest_bearing_collateral_burn_event(self):
        pass

    def parse_interest_bearing_collateral_mint_event(self, event_data: list[Any]) -> BearingCollateralMintEventData:
        """
        Parses the BearingCollateralMint event data into a human-readable format using the BearingCollateralMintEventData serializer.
        
        The event data is fetched from on-chain logs and is structured in the following way:
        - event_data[0]: The user address (as a hexadecimal string).
        - event_data[1]: Token amount

        Args:
            event_data (list[Any]): A list containing the raw event data, typically with 3 or more elements:
                user address, amount of tokens
        Returns:
            BearingCollateralMintEventData: A Pydantic model with the parsed and validated event data in a human-readable format.

        """
        return BearingCollateralMintEventData(
            user=event_data[0],
            amount=event_data[1],
        )

    def parse_interest_bearing_collateral_burn_event(self, event_data: list[Any]) -> BearingCollateralBurnEventData:
        """
        Parses the BearingCollateralMint event data into a human-readable format using the BearingCollateralMintEventData serializer.
        
        The event data is fetched from on-chain logs and is structured in the following way:
        - event_data[0]: The user address (as a hexadecimal string).
        - event_data[1]: Token amount

        Args:
            event_data (list[Any]): A list containing the raw event data, typically with 3 or more elements:
                user address, amount of tokens
        Returns:
            BearingCollateralMintEventData: A Pydantic model with the parsed and validated event data in a human-readable format.

        """
        return BearingCollateralBurnEventData(
            user=event_data[0],
            amount=event_data[1],
        )

    def parse_debt_transfer_event(self):
        pass

    def parse_debt_mint_event(self, event_data: list[Any]) -> DebtMintEventData:
        """
        Parses the debt mint event data into a human-readable format using the
        DebtMintEventData serializer.

        Args:
            event_data (List[Any]): A list containing the raw debt mint event data,
                                    typically with 2 elements: user and amount.

        Returns:
            DebtMintEventData: A Pydantic model with the parsed and validated event data in a human-readable format.
        """
        return DebtMintEventData(
            user=event_data[0],
            token=event_data[1]
        )

    def parse_debt_burn_event(self, event_data: list[Any]) -> DebtBurnEventData:
        """
        Parses the debt burn event data into a human-readable format using the
        DebtBurnEventData serializer.

        Args:
            event_data (List[Any]): A list containing the raw debt burn event data,
                                    typically with 2 elements: user and amount.

        Returns:
            DebtBurnEventData: A Pydantic model with the parsed and validated event data in a human-readable format.
        """
        return DebtBurnEventData(
            user=event_data[0],
            amount=event_data[1]
        )