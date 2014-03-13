<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="13008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="BallShear_BallSelection.vi" Type="VI" URL="../BallShear_BallSelection.vi"/>
		<Item Name="BallShear_BallShear.vi" Type="VI" URL="../BallShear_BallShear.vi"/>
		<Item Name="BallShear_DependencyCheck.vi" Type="VI" URL="../BallShear_DependencyCheck.vi"/>
		<Item Name="BallShear_main.vi" Type="VI" URL="../BallShear_main.vi"/>
		<Item Name="BallShear_PackageAnalysis.vi" Type="VI" URL="../BallShear_PackageAnalysis.vi"/>
		<Item Name="BallShear_PackageCapture.vi" Type="VI" URL="../BallShear_PackageCapture.vi"/>
		<Item Name="BallShear_PackageCheck.vi" Type="VI" URL="../BallShear_PackageCheck.vi"/>
		<Item Name="BallShear_ResultDisplay.vi" Type="VI" URL="../BallShear_ResultDisplay.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="System.Windows.Forms" Type="Document" URL="System.Windows.Forms">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
